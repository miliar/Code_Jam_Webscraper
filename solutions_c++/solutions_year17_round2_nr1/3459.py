#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream input;
    input.open("A-large (1).in");
    ofstream output;
    output.open("22codejam.txt");
double t;
input>>t;long j;
for(j=0;j<t;j++)
{
double d,q,w;long n,i;
input>>d>>n;
double k[n],s[n],max=0,e;
for(i=0;i<n;i++)
{input>>k[i]>>s[i];
q=d-k[i];
w=q/s[i];

if(w>max)
    max=w;


} e=d/max;
output<<"Case #"<<j+1<<": "<<fixed<<setprecision(6)<<e<<endl;
//printf("Case #%d: %lf\n",j+1,e);
}}
