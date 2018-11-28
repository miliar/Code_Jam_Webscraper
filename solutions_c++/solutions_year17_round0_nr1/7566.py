
#include <iostream>
using namespace std;
const int INF = -1;


int flips(int a[], int M, int N) {
    int s[M] = {0};
    int sum=0, ans=0;
    for(int i=0; i<M; i++) {
        s[i] = (a[i]+sum)%2 != 1;

        sum += s[i] - (i>=N-1?s[i-N+1]:0);

        ans += s[i];

        if(i>M-N and s[i]!=0) return INF;
    }   
    return ans;
}

int main() {
    int T;
    cin >> T;
    string str;
    int K;
    int arr[1000];
    for(int i=0; i<T; i++) {
        cin >> str >> K;
        const int len = str.length();
        for(int j=0; j<len; j++) {
                arr[j] = (str[j] == '+')  ? 1: 0;
		}

        int res = flips(arr, len, K);
	
		if(res != INF) {
			cout << "Case #"<< i+1 << ": " << res << "\n";
		} else {
			cout << "Case #"<< i+1 << ": IMPOSSIBLE""\n";
		}
	}
} // main()



