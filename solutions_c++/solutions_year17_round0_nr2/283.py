#include <bits/stdc++.h>

using namespace std;

int main(){
	// freopen("B-large.in","r",stdin);
	// freopen("answer.txt","w",stdout);
	cin.sync_with_stdio(0); cin.tie(0);
	int T; cin >> T;
	for (int tc = 1; tc <= T; ++tc){
		string S; cin >> S;
		int arr[19];
		arr[0] = -1e9;
		for (int i=0; i<S.length(); ++i){
			arr[i+1] = S[i] - '0';
		}
		int ed = -1;
		for (int i=1; i<=S.length(); ++i){
			if (arr[i-1] > arr[i]){
				ed = i-1; //bad # lol
				break;
			}
		}
		if (ed != -1){
			int beg = ed;
			while (arr[beg-1] == arr[ed]){
				beg--;
			}
			arr[beg]--;
			for (int i=beg+1; i<=S.length(); ++i){
				arr[i] = 9;
			}
		}
		printf("Case #%d: ", tc);
		if (arr[1] != 0) printf("%d", arr[1]);
		for (int i=2; i<=S.length(); ++i){
			printf("%d", arr[i]);
		}
		printf("\n");
	}
	return 0;
}