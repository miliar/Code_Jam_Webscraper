#include <bits/stdc++.h>
#define us unordered_set
#define os ordered_set
#define om ordered_map
#define um unordered_map
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define rmod 1000000
using namespace std;
double tim=0.0;
double maximum(double a,double b)
{
    if(a>b)
        return a;
    else return b;
}
struct horse
{int speed,distance;
};
struct comp
{
    bool operator()(const horse &a,const horse &b)
    {
        if(a.distance>=b.distance)
            return false;
        else return true;
    }
}compa;

vector<horse> ho;
int main()
{freopen("input.IN","r",stdin);
freopen("jam.txt","w",stdout);
    int t;
scanf("%d",&t);
int index=0;
while(t--)
{index++;
    int n,d;
    scanf("%d%d",&d,&n);
    ho.clear();
    for(int i=1;i<=n;i++)
    {
        int k,s;
        horse temp;
        scanf("%d%d",&k,&s);
        temp.distance=k;
        temp.speed=s;
        ho.pb(temp);
    }
tim=0.0;
sort(ho.begin(),ho.end(),compa);
int prev,prevdis;
for(int i=n-1;i>=0;i--)
{horse temp=ho[i];
if(i==(n-1))
    {tim=(double)(d-temp.distance)/(double)temp.speed;
    prev=temp.speed;
    prevdis=temp.distance;}
    if(temp.speed<=prev)
    {
        prev=temp.speed;
        tim=(double)(d-temp.distance)/(double)temp.speed;
        prevdis=temp.distance;
    }
    else
        {
        double tr=(double)(d-temp.distance)/(double)temp.speed;
        double tem=(double)(prevdis-temp.distance)/(double)(temp.speed-prev);
        double tocheck=tem;
        if((prevdis+tem*prev)>d)
        tocheck=tr;
        tim=maximum(tim,tocheck);
    }

}
double finalspeed=d/tim;
printf("Case #%d:%lf\n",index,finalspeed);

}
return 0;}
