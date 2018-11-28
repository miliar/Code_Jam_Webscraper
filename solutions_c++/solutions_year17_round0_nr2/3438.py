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
#define ll long long

#define REP(i,n) for(;i<n;i++)
#define REP3(i,a,b) for(i=a;i<b;i++)
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;



bool istidy(string &sc)
{
    for(int i=0;i<sc.size()-1;i++)
    {
        if(sc[i]>sc[i+1])
            return false;
    }
    return true;
}

string conv2str(ll n)
{
    string sc;
    while(n!=0)
    {
        int r = n%10;
        sc.push_back((char)('0'+r));
        n = n/10;
    }
    reverse(sc.begin(),sc.end());
    return sc;
}

int arr[20];
int minm[20];

int getlength(ll n)
{
    int x=0;
    int i=0;
    while(n!=0)
    {
        int r = n%10;
        arr[i] = r;
        i++;
        n = n/10;
        x++;
    }
    return x;
}

void solve()
{
    ll n;
    cin>>n;

    string sc = conv2str(n);

    if(istidy(sc))
    {
        cout<<sc;
        return;
    }

    int l  =getlength(n);
    reverse(arr,arr+l);

    //cout<<arr[0]<<" "<<arr[1]<<endl;

    for(int i=l-1;i>=1;i--)
    {
        //if i
        if(arr[i-1]>arr[i])
        {
            arr[i-1]--;
            for(int j=i;j<l;j++)
            {
                arr[j]=9;
            }
        }
    }















/*


    minm[l-1] = arr[l-1];

    for(int i=l-2;i>=0;i--)
    {
        minm[i] = min(arr[i],minm[i+1]);
    }
    for(int i=0;i<l;i++)
    {
        arr[i] = minm[i];
    }*/

    ll ans = 0;

    for(int i=0;i<l;i++)
    {
        ans = ans*10;
        ans = ans+arr[i];
    }

    cout<<ans;

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
