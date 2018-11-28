#include <bits/stdc++.h>
using namespace std;
int main() {
	int t;
	cin >> t;
	for(int n,k,h=1;h<=t;h++) {
		cin >> n >> k;
		vector <int> s;
		s.push_back(0);
		s.push_back(n+1);
		int m1,m2,number;
		while(k--) {
			int mi=-1,ma=-1,num1=-1,num2=-1,flag1=0,flag2=0,flag=0,num,miA,maA,miA1,maA1,miA2,maA2;
			for(int i=0;i<s.size()-1;i++) {
				if(s[i+1]-s[i]>1) {
					int mid = s[i]+ (s[i+1]-s[i])/2;
					int l = mid-s[i];
					int r = s[i+1]-mid;
					//cout << s[i] << " " << s[i+1] << endl;
					//cout << mid << " " << l << " " << r << endl;
					if(!flag) {
						flag = 1;
						num =  mid;
						maA = max(l,r);
						miA = min(l,r);
					}
					if(min(l,r)>mi) {
						if(mi!=-1)flag1 =1 ;
						mi = min(l,r);
						num1 = mid;
						maA1 = max(l,r);
						miA1 = min(l,r);
					} else if(min(l,r)<mi) flag1 = 1;
					if(max(l,r)>ma) {
						if(ma!=-1)flag2 = 1;
						ma = max(l,r);
						num2 = mid;
						maA2 = max(l,r);
						miA2 = min(l,r);
					} else if(max(l,r)<ma) flag2 = 1;
				}
			}
			if(flag1) {
				m1 = maA1;
				m2 = miA1;
				number = num1;
				s.push_back(num1);
				//cout << "flag1" << endl;
			} else if(flag2) {
				m1 = maA2;
				m2 = miA2;
				number = num2;
				s.push_back(num2);
				//cout << "flag2" << endl;
			} else {
				m1 = maA;
				m2 = miA;
				number = num;
				s.push_back(num);
				//cout << "flag" << endl;
			}
			sort(s.begin(),s.end());
			/*for(int i=0;i<s.size();i++) {
			cout << s[i] << " ";
		    }*/
	    }
		//cout << endl;
		//cout << number << " ";
	    cout << "Case #" << h << ": " << m1-1 << " " << m2-1 << endl;
	}
}










/*
 #include <bits/stdc++.h>
using namespace std;
int main() {
	int t;
	cin >> t;
	for(int c=1;c<=t;c++) {
		bool ok = 0;
		string s;
		int n,ans=0;
		cin >> s >> n;
		for(int i=0;i<=s.size()-n;i++) {
			int counter = 0;
			for(int j=i;j<=i+n-1;j++) {
				if(s[j]=='-') counter++;
			}
			if(counter==n) {
				ans++;
				for(int j=i;j<=i+n-1;j++) {
					s[j] = '+';
				}
			}
		}
		for(int i=0;i<s.size()-n;i++) {
			bool flag = 0;
			for(int j=i+1;j<=i+n-1;j++) {
				if(s[j]=='-') flag = 1;
			}
			if(!flag && s[i]=='-' && s[i+n]=='-') {
				ans+=2;
				for(int j=0;j<=i+n;j++) {
					s[j] = '+';
				}
			}
		}
		int cnt = 0;
		for(int i=0;i<s.size();i++) {
			if(s[i]=='+') cnt++;
		}	
		if(cnt==s.size()) ok = 1;
		if(!ok) cout << "Case #" << c << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << c << ": " << ans << endl;	
	}
} */

