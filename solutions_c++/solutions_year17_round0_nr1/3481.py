#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
#include<queue>
#include<unordered_set>
#include<map>
#include<unordered_map>
#include<cstdio>
#include<cmath>
#include<iomanip>
#include<climits>
//#include<bits/stdc++.h>
using namespace std;

#define gc getchar

void scanint(int &x)
{
    register int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}
void scanlint(long long int &x)
{
    register long long int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}
#define pc putchar;
inline void writeInt (int n)
{
    int N = n, rev, count = 0;
    rev = N;
    if (N == 0) { pc('0'); pc('\n'); return ;}
    while ((rev % 10) == 0) { count++; rev /= 10;} //obtain the count of the number of 0s
    rev = 0;
    while (N != 0) { rev = (rev<<3) + (rev<<1) + N % 10; N /= 10;}  //store reverse of N in rev
    while (rev != 0) { pc(rev % 10 + '0'); rev /= 10;}
    while (count--) pc('0');
}
//limits
#define mod 1000000007

void boost()
{
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
}

#define vi vector<int>
#define vlli vector<long long int>
#define pb push_back
#define pii pair<int,int>
#define plli pair<long long int,long long int>
#define lli long long int

#define REP(i,n) for(;i<n;i++)
#define REP3(i,a,b) for(i=a;i<b;i++)

set<int> ss;

void solve()
{
    ss.clear();
    int ans=0;
    string sc;
    cin>>sc;
    int k;
    cin>>k;

    for(int i=0;i<=sc.size()-k;i++)
    {
        //find character;
        char ch = sc[i];
        if(ss.size()==0)
        {
            //same
        }
        else
        {
            if((*(ss.begin()))<i)
            {
                //delete it
                //cout<<"HOLA"<<endl;
                ss.erase(ss.begin());
            }
            int x = ss.size()&1;
            if(x)
            {
                if(ch == '+')
                {
                    ch = '-';
                }
                else
                {
                    ch = '+';
                }
            }
        }
        sc[i] = ch;

        if(sc[i]=='+')
        {
            continue;
        }
        else
        {
            //change
            ans++;
            sc[i]='+';
            ss.insert(i+k-1);
            //cout<<i+k-1<<endl;
        }
    }

    for(int i=(sc.size()-k)+1;i<sc.size();i++)
    {
        //find character;
        char ch = sc[i];
        if(ss.size()==0)
        {
            //same
        }
        else
        {
            if((*(ss.begin()))<i)
            {
                //delete it
                ss.erase(ss.begin());
            }
            int x = ss.size()&1;
            if(x)
            {
                if(ch == '+')
                {
                    ch = '-';
                }
                else
                {
                    ch = '+';
                }
            }
        }
        sc[i] = ch;
    }

    int i;
    for(i=0;i<=sc.size();i++)
    {
        if(sc[i]=='-')
            break;
    }
    //cout<<sc<<" "<<ans<<endl;
    if(i<sc.size())
    {
        cout<<"IMPOSSIBLE";
    }
    else
    {
        cout<<ans;
    }


}

int main()
{

   // cout<< 5000/10*100;
    // return 0;


    cin.tie(0);
	cout.tie(0);
	cin.sync_with_stdio(0);
	cout.sync_with_stdio(0);

	freopen("A-largee.in","r",stdin);
	freopen("output.txt","w",stdout);

	int TC = 1;
	cin>>TC;

	for(int ZZ=1;ZZ<=TC;ZZ++){
		cout<<"Case #"<<ZZ<<": ";
//		double ans;
//		cout.precision(10);
//		cout<<fixed<<ans<<endl;
		solve();
		cout<<endl;
	}
	return 0;

}
