#include<iostream.h>
#include<conio.h>
#include<fstream.h>

int tidy(long num){
 int digit,last=10;
 while(num){
  digit=num%10;
  if(digit>last){
   return 0;
  }
  last=digit;
  num=num/10;
 }
 return 1;
}

long checkLast(long num){
 long last=1;
 int isTidy;
 for(int j=1; j<=num; j++){
  isTidy=tidy(j);
  if(isTidy){
   last=j;
  }
 }
 return last;
}

void main(){
 clrscr();
 long num[100];
 int size,count=-1;
 ifstream read;
 read.open("project/lasttidy/sd.IN");
 while(!read.eof()){
  if(count==-1){
   read>>size;
  }else{
   read>>num[count];
  }
  count++;
 }
 ofstream write;
 write.open("project/lasttidy/sdsol.IN");
 for(int i=0; i<size; i++){
   cout<<"Case #"<<i+1<<": "<<checkLast(num[i])<<endl;
   write<<"Case #"<<i+1<<": "<<checkLast(num[i])<<endl;
 }
 getch();
}