#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
using namespace std;
int main() {
    int T;
    double ans;
    cin >> T;
    int N, K;
    for (int t = 0 ; t < T; ++t) {
	ans = 0.0;
	long long int R[1000], H[1000];
	long long int R_H[1000];
	cin >> N>> K;
	for (int i = 0 ; i < N; ++i) {
	    cin >> R[i] >> H[i];
	    R_H[i] = R[i]*10000000+H[i];
	}
	long long int surface[1000];
	sort(R_H, R_H+N);
	long long int t_R, t_H;
	long long int tmp_ans, max_R;
	for (int i = N-1; i >=K-1; --i) {
	    tmp_ans = 2*(R_H[i]%10000000)*(R_H[i]/10000000);
	    max_R =   R_H[i]/10000000;
//	    cout <<"max_R=" << max_R << endl;
	    for (int j = i-1 ; j >=0; --j ) {
		t_R = R_H[j]/10000000;
		t_H = R_H[j]%10000000;
		surface[j] = 2*t_R*t_H; 
//		cout << t_R << " " << t_H << " " << surface[j]<<endl;
	    }
	    sort(surface, surface+i);
	    for (int j = 0; j < K-1; ++j) {
		tmp_ans += surface[i-1-j];
	    }
	    tmp_ans += max_R*max_R;
//	    cout << tmp_ans << endl;
	    if (ans < tmp_ans) ans = tmp_ans;
	}
//	cout << ans << endl;
//	cout << "max_R="<<max_R<< endl;
//	cout <<(double)max_R*max_R*M_PI << endl;
	ans*=M_PI;
	printf("Case #%d: %.10lf\n", t+1, ans);
//	cout << "Case #" << (t+1) << ": " << ans << endl;
    }

    return 0;
}
