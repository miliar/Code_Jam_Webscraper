#include <iostream>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <stack>
#include <cmath>

#define llt long long int
#define pi 3.14159265358979323846
#define mod 1000000007
#define tsolve int t; cin>>t; while(t--)

#define ind(x) scanf("%d" , &x)
#define inlld(x) scanf("%lld" , &x)
#define outd(x) printf("%d\n" , x)
#define outlld(x) printf("%lld\n" , x)

#define newl printf('\n')
#define spce printf(' ')

using namespace std;

llt integer(string s) {
        llt n=0,i=0;

        while(s[i]!='\0') {
                n=n*10+((int)s[i]-48);
                i++;
        }
        return n;
}

int main() {
    freopen("in.in" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
	int t;
	cin>>t;
	for (int it=1;it<=t;it++) {
	    string n;
	    cin>>n;
	    int flag=0;
	    if (n.size()==1) {
	        cout<<"Case #"<<it<<": "<<n<<endl;
	        continue;
	    }
	    for (int j=1;j<n.size();j++) {
	    	if (n[j]<n[j-1])
	    	{
	    		flag=1;
	    		break;
	    	}
	    }
	    if (flag==0)
	    cout<<"Case #"<<it<<": "<<integer(n)<<endl;
	    else {
	    	for (int i=0;i<n.size()-1;i++) {
	    	    if (n[i]>=n[i+1]) {
	    	        n[i]=n[i]-1;
	    	        for (int j=i+1;j<n.size();j++)
		             n[j]='9';
		            break;
	    	    }
	    	}
	    	cout<<"Case #"<<it<<": "<<integer(n)<<endl;
	    }
	}
	return 0;
}
