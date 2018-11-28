#include<bits/stdc++.h>
using namespace std;
int t_cases;

void checkTidy(string s){
bool flag=false;
 for(int i=0; i<s.length()-1; i++){
  if(((int)s[i]-'0')>((int)s[i+1]-'0')){ flag=true; break;}
 }
if(flag){
 cout<<" False"<<endl;
 }
else{
 cout<<" True"<<endl;
}
}

string tidyNum(string num){

long long n=num.length();
int rDigit;bool flag=false;
long long i=0;

for(i=0; i<n-1; i++){

if((int)num[i]>(int)num[i+1]){

 rDigit=(int)num[i]-49; flag=true; break;

}
}
if(flag){  //do replacement
 string str=num;
 //cout<<rDigit<<endl;
 if(rDigit==0){

  num.resize(n-1);
  for(long long j=0; j<n; j++) num[j]='9';
 }
 else if(rDigit==8){

     long long j=i;
     while(num[j]=='9'&&j>=0){
        j--;
     }
     num[j+1]='8';
 for(j=i+1; j<n; j++) num[j]='9';
  }

else{

 //num[i]=rDigit+'0';
 long long j=i;
 while( j>=1 && ( (int)num[j-1]-48 )>rDigit) j--;
 num[j]=rDigit+'0';
 for(j=j+1; j<n; j++) num[j]='9';
}
return num;

}
else{
return num;
 }
}


int main(){



int t_case;
 cin>>t_case;
 string s;
 string s2;
 for(t_cases=1; t_cases<=t_case; t_cases++){
  cin>>s;
  s2=tidyNum(s);
  cout<<"Case #"<<t_cases<<": "<<s2<<endl;
  //checkTidy(s2);
  }
 return 0;
}

