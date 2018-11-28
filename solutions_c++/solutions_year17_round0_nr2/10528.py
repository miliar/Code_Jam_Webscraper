#include<bits/stdc++.h>
using namespace std;
int tidy(unsigned long long  n)
{vector<int> v;
while(n)
{int x=n%10;
v.push_back(x);
n=n/10;
}
int l=v.size();
int y=1;
for(int i=0; i<l-1; i++)
{
    if(v[i]<v[i+1])
        y=0;
}
return y;
}
int main()
{FILE *p,*q;
p=fopen("input.txt","r");
q=fopen("output.txt","w");
int t;
fscanf(p,"%d\n",&t);
for(int i=1; i<=t; i++)
{unsigned long long n;
fscanf(p,"%d\n",&n);
unsigned long long ans=n;
while(!tidy(n))
{n-=1;
ans=n;
}
cout<<ans<<endl;
fprintf(q,"Case #%d: %d\n",i,ans);
}
fclose(p);
fclose(q);
return 0;
}
