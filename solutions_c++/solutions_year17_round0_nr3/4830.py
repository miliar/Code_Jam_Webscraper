#include <bits/stdc++.h>
#include <string>
#define lli long long int
#define vi vector <int>
#define pb push_back
#define mp make_pair
#define vpii vector < pair <int, int> >
#define pii pair <int, int>
using namespace std;

int displayvi(vi a){for(int i=0;i<a.size();i++) cout<<a[i]<<"-"; cout<<endl;}

lli two(int
i)
{
    return pow(2,i);
}

lli twom1(int i)
{
    return pow(2,i)-1;
}

int pow2(lli k)
{
    lli i=1; int j=1;
    while(i<k){i=i*2+1; j++;}
    return j;
}

int display(vpii a)
{
    for(int i=0;i<a.size();i++) cout<<a[i].first<<"-"<<a[i].second<<"\t"; cout<<endl;
}

string to_string(lli i)
{
    if(i==0) return "0";
    if(i<0) return "-"+to_string(-i);
    
    string s;
    while(i>0)
    {
        int r=i/10;
        i=i/10;
        s=""+r+s;
    }
    return s;
}

vpii mergvpii(vpii a)
{
    for(int i=0;i<a.size()-1;i++)
    {
        if(a[i].first==a[i+1].first)
        {
            int k=a[i].second+a[i+1].second;
            pii b=a[i];
            b.second=k;
            a[i]=b;
            a.erase(a.begin()+i+1);
        }
    }
    return a;
}

lli q3(lli n, lli k)
{
    vpii a;
    a.pb(mp(n,1));
    
    while(k>1)
    {
        //display(a);
        //cout<<k<<"^"<<endl;
        
        pii b=a[a.size()-1];
        if(b.second<k)
        {
            a.erase(a.end());
            int nt=b.first;
            if(nt%2==0) {
                a.pb(mp(nt/2,b.second));
                a.pb(mp((nt/2)-1,b.second));
            }
            else
            {
                a.pb(mp(nt/2,2*b.second));
            }
            k=k-b.second;
        }
        else
        {
            b.second=b.second-(k-1);
            a[a.size()-1]=b;
            k=k-(k-1);
            break;
        }
        
        sort(a.begin(),a.end());
        a=mergvpii(a);
    }
    
    return a[a.size()-1].first;
}



int main() {
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        lli n; lli k;
        cin>>n>>k;
        //cin>>k;

        lli a=q3(n,k);
        lli ans1,ans2; ans1=a/2; ans2=a/2;
        if(a%2==0) ans2--;
        
        cout<<"Case #"<<tt<<": "<<ans1<<" "<<ans2<<endl;
    }
	// your code goes here
	return 0;
}
