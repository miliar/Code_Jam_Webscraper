#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
long long arr[100009],has[100009],cnt=0;


#define mp make_pair
#define pb push_back

ll gcd(ll a ,ll b)
{
        if(b%a==0) return a;
        else return gcd(b%a,a);
}
int main()
{
        ll  n,m,i,j,k,a=1,b,x,t,y,z,c, T=1;
        freopen("B-large.in", "r", stdin);
    	freopen("output.out", "w", stdout);
        scanf("%lld",&t);
        while(t--)
        {
                cin>>n;
                char str[100];
                sprintf(str, "%lld", n);m=0;
                for(i=0;i<strlen(str)-1;i++)
                {
                        if(str[i]>str[i+1])
                        {
                                a=str[i]-48;
                                if(a==1){m=1;
                                        j=-1;
                                }
                                else
                                {
                                        for(j=i-1;j>=0;j--)
                                        {
                                                if(str[j]!=str[j+1]) break;
                                        }
                                        str[j+1]--;
                                }
                                for(k=j+2;k<strlen(str);k++) str[k]='9';
                                break;
                        }
                }
	cout<<"Case #"<<T++<<": ";
                if(m==0)
                cout<<str<<endl;
                else {
                        for(j=1;j<strlen(str);j++) cout<<str[j];cout<<endl;
                }
        }
        return 0;
}
