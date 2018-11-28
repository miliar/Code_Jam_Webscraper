#include <bits/stdc++.h>

using namespace std;

// hope for O(logn)
int main(){
	int k;
	cin >> k;
	ofstream out("ofile3");

	for(int p=1;p<=k;p++){
		int n;
		int k;
		cin >> n >> k;

		int l = n%2==0?n/2-1:n/2;
		int r = n/2;

		int cnt = 2;
		int k_dup = k-1;
		if(k_dup==0){
			out << "Case #" << p << ": " << r << " " << l << endl;
			continue;
		}

		bool flag = (l!=r);
		bool flag2 = (r%2!=0);
		double portion = 1.0;
		while(k_dup > 0){
			// do right

		//	cout << cnt << endl;
			cout << r << " " << l << endl;

			if(flag){
				if(flag2){
					portion = portion+(1.0-portion)*1.0/2;
				}else{
					portion = portion*(1.0/2);
				}
			}else{
				portion = 0.5;
			}
			cout << cnt << " " << portion << endl;
			k_dup-=(cnt*portion);
			cout << k_dup << endl;
			if(k_dup <=0){
				out << "Case #" << p << ": " << r/2 << " " << (r%2==0?r/2-1:r/2) << endl;
				break;
			}

			// do left
			k_dup-=(cnt*(1-portion));
			if(k_dup <=0){
				if(l==0){
					out << "Case #" << p << ": " << 0 << " " << 0 << endl;
				}else{
					out << "Case #" << p << ": " << l/2 << " " << (l%2==0?l/2-1:l/2) << endl;
				}
				break;
			}


			flag = (l!=r);
			flag2 = (r%2!=0);

			r = r/2;
			l = l%2==0?l/2-1:l/2;
			cnt *=2;
		}
	}
}