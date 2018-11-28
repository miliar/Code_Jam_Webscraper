#include <bits/stdc++.h>
using namespace std;

int main() 
{int t,op;
cin>>t;
op=t;
while(t--)
{long long k,cp;
cin>>k;

cp=k;
vector <int> a;
while(cp!=0)
{int j=cp%10;
a.push_back(j);
cp=cp/10;
}

for(int i=0;i<a.size();i++)
{if(a[i]<a[i+1]&&a.size()>1)
{a[i]=9;
a[i+1]=a[i+1]-1;
for(int j=0;j<i;j++)
{
a[j]=9;	
}

}
}
long long ans=0;
for(int i=0;i<a.size();i++)
{

ans+=(pow(10,i)*a[i]);
}
cout<<"Case #" <<op-t<<": " <<ans<<endl;    
}
	
}

