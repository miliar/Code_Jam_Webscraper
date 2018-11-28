#include <iostream>
using namespace std;

long long int power2(long long int n)
{
    long long int p = 1;
    if (n && !(n & (n - 1)))
        return n;
    while (p < n)
        p <<= 1;
    return p/2;
}

void call(long long int n){
	if (n == -1) cout << "0 0";
	else if (n%2 == 0) cout << n/2 << " " << n/2;
	else cout << n/2+1 << " " << n/2;
}

void func(){
	long long int N, K; cin >> N >> K;
	long long int J = power2(K);
	if (N%J < K-J) call(N/J-2);
	else call(N/J-1);
}

int main(){
	int T; cin >> T;
	for (int i=0; i<T; i++){
		cout << "Case #" << i+1 << ": "; 
		func();
		cout << endl;
	}
}