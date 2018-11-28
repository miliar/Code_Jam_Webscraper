#include<bits/stdc++.h>
using namespace std;
string s;
long long tunda_kabab;
int main()
{
//  freopen("input.txt","r",stdin);
 //freopen("output.txt","w",stdout);
cin>>tunda_kabab;
for(int lehsun=1;lehsun<=tunda_kabab;lehsun++)
{
  cin>>s;
long long result=0;
vector<long long>jyoti;
for(int i=0;i<s.size();i++)
  {int y=s[i]-'0';jyoti.push_back(y);}
for(int karamjaliyan=0;karamjaliyan<31;karamjaliyan++)
{
for(int i=0;i<jyoti.size()-1;i++)
{
  if(jyoti[i]>jyoti[i+1])
  {
    jyoti[i]--;
    for(int sasur=i+1;sasur<jyoti.size();sasur++)
    jyoti[sasur]=9;
    break;
  }
}
}
for(int i=0;i<jyoti.size();i++)result=result*10+jyoti[i];
cout<<"Case #"<<lehsun<<": "<<result<<endl;
}

  return 0;
}
