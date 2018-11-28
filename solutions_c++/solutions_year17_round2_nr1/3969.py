#include<iostream>
#include<map>
#include<cstdio>
using namespace std;
int main() {
    int TT;
    int D, N;
    double ans;
    cin >> TT;
    int K[1000], S[1000];
    double T[1000], t[1000];
    int p;
    for (int tt = 0 ; tt < TT; ++tt) {
	map <int, int> K_S;
	int change[1000]={0};
	cin >> D >> N;
	for (int i = 0 ; i < N; ++i) {
	    cin >> K[i] >> S[i];
	    K_S.insert(make_pair(K[i],S[i]));
	    change[i] = i;
	}
	int n = 0 ;
	for (auto iter = K_S.rbegin(); iter!=K_S.rend(); ++iter) {
	    K[n] = iter->first; 
	    S[n] = iter->second;
	    n++;
	}
	ans = -1;
	t[0] = T[0] = (double)(D-K[0])/S[0];
	for (int i = 1 ; i < N; ++i) {
	    if (S[i] <=S[i-1]) {
		T[i] = (double)(D-K[i])/S[i];
		continue;
	    }
	    else { // S[i-1] < S[i]
		if ((double)(K[i-1]-K[i])/(S[i]-S[i-1]) > T[i-1]) {//good
		    T[i] = t[i] = (double)(D-K[i])/S[i];
		}
		else { //(K[i-1]-K[i])/(S[i]-S[i-1]) < T[i-1]
		    T[i] = T[i-1];
		    for (int j = change[i-1]; j >=0; --j) {
			if (t[j]*S[j]+K[j] > t[j]*S[i]+K[i]) continue;
			else { //t[i-1]*S[i-1]+K[i-1] <= t[i-1]*S[i]+K[i]
			    t[i] = (double)(K[j]-K[i])/(S[i]-S[j]);
			    change[i] = j;
			    break;
			}
		    }
		}
	    }
	}
	ans =(double) D/T[N-1];
	/*
	for (int i = 0 ; i < N; ++i) {
	    cout << T[i] << endl;
	}
	*/
	printf("Case #%d: %.6lf\n", tt+1, ans);
//	cout << "Case #" << (tt+1) << ": " << ans << endl;
    }

    return 0;
}
