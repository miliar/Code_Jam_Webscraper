#include <iostream>

using namespace std;

int max(int a, int b){
	if(a<b)
		return b;
	else
		return a;
}

int min(int a, int b){
	if(a>b)
		return b;
	else
		return a;
}

int leftN(int *p, int pos){
	int cont = 0;
	while(pos - cont - 1 >= 0 && p[pos-cont - 1] != 1)
		cont++;	
	return cont;
}

int rightN(int *p, int size, int pos){
	int cont = 0;
	while(pos + cont + 1 < size && p[pos+cont + 1] != 1)
		cont++;
	return cont;
}

int main()
{
	int T;
	cin >> T;
	for (int cont = 1; cont < T+1; cont++) {
		int N, K;
		cin >> N;
		cin >> K;
		int stalls[N];
		for (int i = 0; i<N; i++){
			stalls[i] = 0;
		}
		//Populating with K people
		int left, right, maxn,minn;
		maxn = 0;
		minn = 0;

		for(int j = 0; j < K; j++){
			int current = 0;
			maxn = 0;
			minn = 0;
			for(int i = 0; i < N; i++){
				if(stalls[i] == 0){
					left = leftN(stalls, i);
					right = rightN(stalls, N, i);
					if(min(left, right) > minn)	{
						minn = min(left, right);
						maxn = max(left, right);
						current = i;
					}
					else if (min(left, right) == minn){
						if(max(left, right) > maxn){
							maxn = max(left, right);
							current = i;
						}
					}
				}
			}
			stalls[current] = 1;
		}


		cout << "Case #" << cont << ": " << maxn << " " << minn << endl; 
	}

	return 0;
}
