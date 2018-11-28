//An Emperor Production
//in Association with Assistant Professor MR Ram Kripal Mishra.
//Copyright (C) 2017,2015 CodeGeeks, Inc.,
//B-217 KIT, Rooma, Kanpur, INDIA
//Everyone is permitted to copy and distribute verbatim copies
//of this code, but changing it is not allowed.
#include<bits/stdc++.h>
using namespace std;
#define ln pf("\n")
#define I inr()
#define C inc()
#define SS ins()
#define sp pf(" ")
#define loop(i,a,b) for(int i=a;i<b;i++)
#define pool(i,a,b) for(int i=a;i>=b;i--)
#define pb push_back
#define NORM(x) if(x>=MOD)x-=MOD
#define CLR(x,y) memset(x,y,sizeof(x))
#define mp make_pair
#define um unordered_map
#define ppb pop_back()
#define pf printf
#define pi pair<int,int>
#define sf scanf
#define swi switch
#define vec vector
#define veci vector<int>
#define vecs vector<string>
typedef long long ll;
ll MOD = 1000000007;
typedef unsigned long long ull;
typedef string str;
void ins(string &s){getline(cin,s);}
int to_num(string s){return atoi(s.c_str());}
ll power(ll x, ll y){ll temp;if( y == 0)return 1;temp = power(x, y/2)%MOD;if (y%2 == 0)return (temp*temp)%MOD;else{if(y > 0)return (x*temp*temp)%MOD;else return (temp*temp)/x;}}
void to_binary(ll n){if(n==1){cout<<1; return;}to_binary(n>>1);cout<<n%2;}
ll inr(){ll V;cin>>V;return V;}
str ins(){str s;cin>>s;return s;}
char inc(){char c;cin>>c;return c;}

/*int n,k;
int ans=1e9;
um<string,int> mymap;

bool all_set(string s)
{

    for(int i=0;i<n;i++)
        if(s[i]!='+')
        return false;
    return true;
}
int find_min(string s,int cost)
{
    //cout<<s<<endl;
    if(cost > n)
        return 1e9;
    if(all_set(s))
        {
            return ans=min(ans,cost);
        }
   if(!mymap[s]){
    for(int i=0;i<=n-k;i++)
    {

        for(int j=i;j<i+k;j++)
            {
                if(s[j]=='+')
                    s[j]='-';
                else
                    s[j] = '+';
            }

                mymap[s] = min(cost+1,find_min(s,cost+1));


        //find_min(s,cost+1);
         for(int j=i;j<i+k;j++)
            {
                if(s[j]=='-')
                    s[j]='+';
                else s[j]='-';
            }

    }
   }
   return mymap[s]= min(mymap[s],cost);

}
*/
int main()
{
int t=I;
loop(i,0,t)
{
    cout<<"Case #"<<i+1<<": ";
    int a1=0,a2=0;
    int a[100001];
    int k=I;
    int n=I;
    int l=0,r=1;
    a[l]=k;
    while(1)
    {
        a[r] = a[l]/2;
        a[r+1] = a[l]%2?a[l]/2:a[l]/2 - 1;
        if(!a[r] && !a[r+1] && !a[l+1])
            break;

        r+=2;
        l++;

    }

    sort(a,a+r);
    reverse(a,a+r);
    /* loop(i,0,k)
    cout<<a[i]<<" ";ln;*/
    cout<<a[n-1]/2 <<" ";
    a[n-1]%2?cout<<a[n-1]/2:cout<<a[n-1]/2-1;
   ln;
}

}
