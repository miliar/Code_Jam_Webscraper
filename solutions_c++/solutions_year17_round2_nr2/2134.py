#include<iostream>
using namespace std;
int main() {
    int T;
    int ans;
    int type;
    cin >> T;
    for (int t = 0 ; t < T; ++t) {
	int N, R, O, Y, G, B, V;
	char out[1001]={0};
	cin >> N >> R >> O >> Y >> G >> B >> V;
	if (O==0 && G==0 && V==0) type=0;
	if (type==0) {
	    if (R > Y+B || Y > R+B || B > R+Y) {
		cout << "Case #" << (t+1) << ": IMPOSSIBLE"  << endl;
		continue;
	    }
	    cout << "Case #" << (t+1) << ": ";
	    char max,min1,min2;
	    int max_n,min_n1,min_n2;
	    if( R>=Y&&R>=B) {max='R';
		if (Y>=B) {min1='Y';min2='B';min_n1=Y,min_n2=B;}
		else      {min2='Y';min1='B';min_n2=Y,min_n1=B;}
		max_n = R;}
	    if( Y>=R&&Y>=B) {max='Y';
		if (R>=B) {min1='R';min2='B';min_n1=R,min_n2=B;}
		else      {min2='R';min1='B';min_n2=R,min_n1=B;}
		max_n = Y;}
	    if( B>=R&&B>=Y) {max='B';
		if (Y>=R) {min1='Y';min2='R';min_n1=Y,min_n2=R;}
		else      {min2='Y';min1='R';min_n2=Y,min_n1=R;}
		max_n = B;}
	    for (int i = 0 ; i < max_n*2; ++i) {
		if (i%2==0) out[i]=max;
		else {
		    if (min_n1>=min_n2){
			out[i] = min1;
			min_n1--;
		    }
		    else {
			out[i] = min2;
			min_n2--;
		    }
		}
	    }
	    for (int i = max_n*2; i < N; ++i) {
		if (min_n1>=min_n2){
		    out[i] = min1;
		    min_n1--;
		}
		else {
		    out[i] = min2;
		    min_n2--;
		}
	    }
	    out[N] ='\0';
	}
	else {
	}
	cout << out << endl;
    }

    return 0;
}
