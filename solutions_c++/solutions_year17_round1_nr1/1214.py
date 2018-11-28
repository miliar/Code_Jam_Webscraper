#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
	int T;
	cin >> T;
	for (int K = 1; K <= T; K++){
		int a, b;
		cin >> a >> b;
		char q[30][30];
		vector<int> em;
		for (int i = 0; i < a; i++){
			for (int j = 0; j < b; j++){
				cin >> q[i][j];
			}
			for (int j = 0; j < b; j++){
				if (q[i][j] != '?'){
					for (int k = 0; k < j; k++)
						q[i][k] = q[i][j];
					em.push_back(i);
					break;
				}
			}
			int pre = b - 1;
			for (int j = b - 1; j >= 0; j--){
				if (q[i][j] != '?'){
					for (int k = pre; k > j; k--)
						q[i][k] = q[i][j];
					pre = j - 1;
				}
			}
			
		}
		int pre = 0;
		for (int i = 0; i < em.size(); i++){
			int r = em[i];
			for (int j = pre; j < r; j++){
				for (int k = 0; k < b; k++){
					q[j][k] = q[r][k];
				}
			}
			pre = r + 1;
		}
		for (int i = pre; i < a; i++){
			for (int j = 0; j < b; j++){
				q[i][j] = q[pre - 1][j];
			}
		}
		cout << "Case #" << K << ":" << endl;
		
		for (int i = 0; i < a; i++){
			for (int j = 0; j < b; j++)
				cout << q[i][j];
			cout << endl;
		}
	}
	
	return 0;
}
