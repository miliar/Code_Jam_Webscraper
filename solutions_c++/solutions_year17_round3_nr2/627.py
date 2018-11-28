#include <bits/stdc++.h>

#define ll long long
#define ld long double

#define all(x) x.begin(),x.end()

using namespace std;

const int mod = 1e9+7;
const ld pi = 3.14159265358979;
const int tot = 24*60;

struct pp
{
	int x,y,z;
};

int n,m;
pp a[200];
int res;

int main()
{
   	ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    cout<<fixed<<setprecision(10);
    
    int testno;
    cin>>testno;
    for(int testi=1; testi<=testno; testi++)
    {
    	int l,r;
    	l = r = 12*60;
    	res=0;
    	
    	cin>>n>>m;
    	for (int i=0; i<n; i++)
    		cin>>a[i].x>>a[i].y,a[i].z=0,l-=a[i].y-a[i].x;
    		
    	int k = n+m;

    	for (int i=0; i<m; i++)
    		cin>>a[n+i].x>>a[n+i].y,a[i+n].z=1,r-=a[i+n].y-a[i+n].x;
    		
    	sort(a,a+n+m,[](pp x, pp y){ return x.x<y.x; });
    	
    	for (int i=0; i<n+m; i++)
    		res+=(a[i].z != a[(i+1)%(n+m)].z);

		vector<int> va,vb,vc;
		
    	for (int i=0; i<k; i++)
    	{
    		int j = (i+1)%k;
    		if (a[i].z==a[j].z && a[i].z==0)
    			va.push_back(  (a[j].x-a[i].y+tot)%tot   );
    		else if (a[i].z==a[j].z && a[i].z==1)
    			vb.push_back(  (a[j].x-a[i].y+tot)%tot   );
    		else vc.push_back(  (a[j].x-a[i].y+tot)%tot  );
    	}
    	
    	sort(all(va)); reverse(all(va));
    	sort(all(vb)); reverse(all(vb));
    	sort(all(vc)); reverse(all(vc));
    	
		for (int i:va) l-=i;
		for (int i:vb) r-=i;
		for (int i:vc) l-=i,r-=i;
		
		if (l>0)
		{
			for (int i:vb) if (l<=0) break; else l-=i,res+=2;		
		} else 
		{
			for (int i:va) if (r<=0) break; else r-=i,res+=2;
		}
    
    	cout<<"Case #"<<testi<<": ";
    	cout<<res;
    	cout<<'\n';
    	
    	cerr<<"Case #"<<testi<<": ";
    	cerr<<res;
    	cerr<<'\n';
    }
    return 0;
}
