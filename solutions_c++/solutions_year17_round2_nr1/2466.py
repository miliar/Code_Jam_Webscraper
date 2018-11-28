#include<bits/stdc++.h>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("out112.txt");
int main()
{
long long t;
fin>>t;
long long l;
l=1;
while(t--)
{
long long d;
fin>>d;
long long n;
fin>>n;
double time=0;
for(long long i=0;i<n;i++)
{
double dis;
double speed;
fin>>dis>>speed;
time=max(time,((double)((d-dis)/speed)));
}
double ans=(d/time);
fout<<"Case #"<<l<<": ";
fout<<fixed<<setprecision(6)<<ans<<"\n";
l++;
}
}
