#define bluetooth Serial

int red = 9;       // LOW = on, HIGH = off
int green = 10;    // LOW = on, HIGH = off
int blue = 11;     // LOW = on, HIGH = off
int r2=3;
int g2=5;
int b2=6;
char cmd[100];
int cmdIndex;

void exeCmd() {
  
  if( (cmd[0]=='r' || cmd[0]=='g' || cmd[0]=='b' || cmd[0]=='x' || cmd[0]=='y' || cmd[0]=='z') && cmd[1]==' ' ) {
    // "r", "g", "b" are the ids for red, green and blue    
       int tval=0;
       String Sval;
       for(int i=2; cmd[i]!=0; i++) {
         Sval=Sval+(cmd[i]);
         
       }
       //Serial.println(Sval);
       tval=Sval.toInt();
       // if cmd is "r 100", val will be 100        
       if(cmd[0]=='r') analogWrite(red, 255-tval);
       if(cmd[0]=='g') analogWrite(green, 255-tval);
       if(cmd[0]=='b') analogWrite(blue, 255-tval);
       if(cmd[0]=='x') analogWrite(r2, 255-tval);
       if(cmd[0]=='y') analogWrite(g2, 255-tval);
       if(cmd[0]=='z') analogWrite(b2, 255-tval);
  } 
}

void setup() {
  
  delay(500); // wait for bluetooth module to start

  bluetooth.begin(115200); // Bluetooth default baud is 115200
  
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  
  digitalWrite(red, HIGH);  // off
  digitalWrite(green, HIGH);  // off
  digitalWrite(blue, HIGH);  // off

  pinMode(r2, OUTPUT);
  pinMode(g2, OUTPUT);
  pinMode(b2, OUTPUT);
  
  digitalWrite(r2, HIGH);  // off
  digitalWrite(g2, HIGH);  // off
  digitalWrite(b2, HIGH);  // off
  
  cmdIndex = 0;
}

void loop() {
  
  if(bluetooth.available()) {
    
    char c = (char)bluetooth.read();
    
    if(c=='\n') {
      cmd[cmdIndex] = 0;
      exeCmd();  // execute the command
      cmdIndex = 0; // reset the cmdIndex
    } else {      
      cmd[cmdIndex] = c;
      if(cmdIndex<99) cmdIndex++;
    }
  }
}
