#include <iostream>

using namespace std;

#define AmanJain jainaman224

int main(){
	int total, testcase, ans1, ans2, a[1001], b[1001], n, m, c, s, p, max1;
	cin >> testcase;
	for(int i=1;i<=testcase;i++){
		cin >> n >> c >> m;
		for(int j=0;j<1001;j++){
			a[j]=b[j]=0;
		}
		max1=0;
		for(int j=0;j<m;j++){
			cin >> p >> s;
			a[p]++;
			b[s]++;
			if(b[s]>max1)
				max1=b[s];
		}
		total=0;
		ans1=(m+n-1)/n;
		ans2=0;
		if(max1>(m+n-1)/n)
			ans1=max1;
		for(int j=1;j<=n;j++){
			if(total+a[j]>j*ans1)
				ans1=(total+a[j])/j;
			total+=a[j];
		}
		for(int j=1;j<=n;j++){
			if(a[j]>ans1)
				ans2+=a[j]-ans1;
		}
		cout << "Case #" << i << ": " << ans1 << " " << ans2 << endl;
	}
	return 0;
}