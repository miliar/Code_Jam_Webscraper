      #include <iostream>
#include<bits/stdc++.h>
#include<string.h>
int a[10];
 using namespace std;
int main(){
int t;
cin>>t;
//cout<<t;
int j=1;
while(j<=t){
string s;
cin>>s;
int k;
cin>>k;
int l=s.length();
int i=0;
int count=0;
for(i=0;i<l;i++){
if(s[i]=='-' && i+k<=l){
count++;
int q;
for(q=0;q<k;q++){
if(s[i+q]=='-')
s[i+q]='+';
else
s[i+q]='-';
//cout<<s<<" ";

}
//cout<<endl;
}

if(s[i]=='-' && i+k>l)
break;
}

if(i!=l)
cout<<"Case #"<<j<<": IMPOSSIBLE";
else


cout<<"Case #"<<j<<": "<<count;

j++;
cout<<endl;
}
return 0;
    }
