#include <Servo.h>

Servo serv1,serv2;

int pos1;
int pos2;

void setup() {
  serv1.attach(9);
  serv2.attach(10);
  Serial.begin(9600);

}

void loop() {
  if(Serial.available()>=0)
  {
    String pystring = Serial.readStringUntil('\n');
    if (pystring=="M1")
    {
      String pystring=Serial.readStringUntil('\n');
      pos1=pystring.toInt();
      serv1.write(pos1);
    }
    
    if (pystring=="M2")
    {
      String pystring=Serial.readStringUntil('\n');
      pos2=pystring.toInt();
      serv2.write(pos2);
    }
  
  }
}
