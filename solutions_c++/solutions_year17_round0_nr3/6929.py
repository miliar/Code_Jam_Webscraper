#include <bits/stdc++.h>
#include <set>
//#define sc(n) scanf("%lld", &n)
#define sc fastscan
#define pr(n) printf("%lld\n", n)
#define ll unsigned long long
#define MP make_pair 
using namespace std;
typedef pair<int, pair<int, int> > PPI;
int n, k;
set<PPI> ms;
void fastscan(int &number)
{
    //variable to indicate sign of input number
    bool negative = false;
    register int c;
 
    number = 0;
 
    // extract current character from buffer
    c = getchar();
    if (c=='-')
    {
        // number is negative
        negative = true;
 
        // extract the next character from the buffer
        c = getchar();
    }
 
    // Keep on extracting characters if they are integers
    // i.e ASCII Value lies from '0'(48) to '9' (57)
    for (; (c>47 && c<58); c=getchar())
        number = number *10 + c - 48;
 
    // if scanned input has a negative sign, negate the
    // value of the input number
    if (negative)
        number *= -1;
}
int main() {
	FILE *fp;
	fp = fopen("Out.txt", "w");
	int test;sc(test);
	for(int t=1; t<=test; ++t) {
		sc(n);sc(k);
		ms.insert(make_pair(-k, make_pair(1, n)));
		for(int i=1; i<=k; ++i) {
			//cout<<"hello"<<endl;
			PPI pp=*ms.begin();
			ms.erase(ms.begin());
			int s=-pp.first, l=pp.second.first, r=pp.second.second;
			int mid=(l+r)/2;
			if(i==k) {
				int mini=min(mid-l, r-mid);
				int maxi=max(mid-l, r-mid);
				fprintf(fp, "CASE #%d: %lld %lld\n", t, maxi, mini);
				//outfile<<"CASE #"<<t<<": "<<maxi<<" "<<mini<<endl;
				ms.clear();
				break;
			}
			if(mid-l>0)
			ms.insert(MP(-(mid-l), MP(l, mid-1)));
			if(r-mid>0)
			ms.insert(MP(-(r-mid), MP(mid+1, r)));
		}
	}
}

