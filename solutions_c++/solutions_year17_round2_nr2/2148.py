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
#include<cstring>
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

#define REP(i,n) for(;i<n;i++)
#define REP3(i,a,b) for(i=a;i<b;i++)
#define ll long long
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define pb push_back
#define mp make_pair

priority_queue<pair<ll,int> > pq;
vector<pair<ll,int> > vc;



void solve()
{
    ll n;
cin>>n;
ll no=n;
ll r,o,y,g,b,v;
cin>>r>>o>>y>>g>>b>>v;
string ans="";
bool valid=true;
char ch='x';
while(n--)
{
    if(ch=='r')
    {
        if(g>0)
        {
            ans.append("G");
            g--;
            ch='g';
        }
        else if(b>y && b>0)
        {
            ans.append("B");
            b--;
            ch='b';
        }
        else if(y>0)
        {
             ans.append("Y");
            y--;
            ch='y';
        }
        else
        {
            valid=false;
            break;
        }

    }

    else if(ch=='o')
    {
        if(b>0)
        {
            ans.append("B");
            b--;
            ch='b';
        }
        else
        {
            valid=false;
            break;
        }
    }
      else if(ch=='g')
    {
        if(r>0)
        {
            ans.append("R");
            r--;
            ch='r';
        }
        else
        {
            valid=false;
            break;
        }
    }
     else if(ch=='v')
    {
        if(y>0)
        {
            ans.append("Y");
            y--;
            ch='y';
        }
        else
        {
            valid=false;
            break;
        }
    }
    else if(ch=='y')
    {
        if(v>0)
        {
            ans.append("V");
            v--;
            ch='v';
        }
        else if(b>r && b>0)
        {
            ans.append("B");
            b--;
            ch='b';
        }
        else if(r>0)
        {
             ans.append("R");
            r--;
            ch='r';
        }
        else
        {
            valid=false;
            break;
        }

    }
    else if(ch=='b')
    {
        if(o>0)
        {
            ans.append("O");
            o--;
            ch='o';
        }
        else if(r>y && r>0)
        {
            ans.append("R");
            r--;
            ch='r';
        }
        else if(y>0)
        {
             ans.append("Y");
            y--;
            ch='y';
        }
        else
        {
            valid=false;
            break;
        }

    }
    else if(r>0)
    {
        ch='r';
        ans.append("R");
        r--;

    }
    else if(y>0)
    {
        ch='y';
        ans.append("Y");
        y--;
    }
     else if(b>0)
    {
        ch='b';
        ans.append("B");
        b--;
    }
    else
    {
        if(n>1)
        {
            valid=false;
        }
           else
        {
            if(o>0)
            {
              if(ans[0]=='B')
              {
                  ans.append("O");
                  o--;
              }
              else
              {
                  valid=false;
              }
            }
            else if(g>0)
            {
                if(ans[0]=='R')
              {
                  ans.append("G");
                  g--;
              }
              else
              {
                  valid=false;
              }
            }
            else
            {
                 if(ans[0]=='Y')
              {
                  ans.append("V");
                  v--;
              }
              else
              {
                  valid=false;
              }
            }
       }
    }
}

if(valid)
{
   char c=ans[0];
    if(c=='O')
    {
        if(ans[no-1]!='B')
        {
            valid=false;
        }
    }
    else if(c=='G')
    {
       if(ans[no-1]!='R')
        {
            valid=false;
        }
    }
    else if(c=='V')
    {
       if(ans[no-1]!='Y')
        {
            valid=false;
        }
    }
    else if(c=='Y')
    {
       if(ans[no-1]!='R' && ans[no-1]!='B' && ans[no-1]!='V')
        {
            valid=false;
        }
    }
    else if(c=='R')
    {
       if(ans[no-1]!='Y' && ans[no-1]!='B' && ans[no-1]!='G')
        {
            valid=false;
        }
    }
    else
    {
               if(ans[no-1]!='Y' && ans[no-1]!='R' && ans[no-1]!='O')
        {
            valid=false;
        }
    }

}
if(valid){
  cout<<ans;

}
else
{
    cout<<"IMPOSSIBLE";
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
