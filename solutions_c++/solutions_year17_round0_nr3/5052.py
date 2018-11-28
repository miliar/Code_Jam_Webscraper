#include<bits/stdc++.h>// <3 Nandini <3
using namespace std;
#define gc getchar
#define mp make_pair
#define pb push_back
#define sc scanint
#define dc print_int
#define f first
#define s second
#define ret return 0;
#define rf std::ios::sync_with_stdio(false);
#define mi 1000000007
#define tl int t;sc(t);while(t--)
#define in int n;sc(n);
#define vin vi arr; for(int i=0;i<n;i++){int a;sc(a);arr.pb(a);}
#define st string s1; getline(cin>>ws,s1);
#define sorta sort(arr.begin(),arr.end());
#define reva reverse(arr.begin(),arr.end());
#define pf(a) printf("%d",a);
#define mina *min_element(arr.begin(),arr.end())
#define maxa *max_element(arr.begin(),arr.end())
#define sl scanlong
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long int lulu;
typedef pair<int, int> pii;
typedef unsigned long long int ull;


void scanint(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}
void scanlong(ull &x);
void scanlong(ull &x)
{
        int flag=0;
        register int c = gc();
        if(c == '-') flag=1;
	x = 0;
	for(;(c<48 || c>57);c = gc());
	for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
        if(flag == 1)x=-x;
}
lulu nu,k;
lulu numb,tempo;
lulu deepu[101];
lulu arru[101];
int main()
{
	int test;
	int i;
	sc(test);
	for(i=1;i<=test;i++)
	{
		scanf("%lld",&nu);
		scanf("%lld",&k);
		int countu = -1;
		arru[0]=nu/2;
		numb=k;
		if(nu%2==0)
        {
            deepu[0]=1;
        }
		else
        {
            deepu[0]=2;
        }

		while(numb!=0)
		{
        numb=numb/2;
        countu++;
		}
		for(int jas=0;jas<countu;jas++)
		{
			if(arru[jas]%2==0)
            {
                deepu[jas+1]=deepu[jas];
            }
			else
            {
                deepu[jas+1]=deepu[jas] + pow(2,jas+1);
            }
			arru[jas+1]=arru[jas]/2;
		}


		if(deepu[countu]<k+1-pow(2,countu))
        {
            cout << "Case #";
            cout<<i<< ": "<< arru[countu]-1 << " " << arru[countu]-1 <<"\n";
        }
		else if (deepu[countu]>= k+1 )
        {
            cout << "Case #" << i << ": " ;
            cout<<arru[countu]<<" " << arru[countu]<<endl;
        }
		else
        {

    cout<< "Case #"<<i <<": ";
    cout<<arru[countu]<< " "<< arru[countu]-1<< endl;
        }
	}
	return 0;
}
