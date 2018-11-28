#include <bits/stdc++.h>
#define lli long long int
using namespace std;


int main(int argc, char const *argv[])
{
	lli i=1,t,j,N, R, O, Y, G, B,V;
	char last;
	cin >> t;
	while(i<=t){
		cin >> N >> R >> O >> Y >> G >> B >> V; 
		cout << "Case #" << i << ": ";
		if(R > N/2 || Y > N/2 || B > N/2) cout << "IMPOSSIBLE\n";
		else{
			lli mini = min(Y,min(R,B));
			lli maxi = max(B,max(R,Y));
			if(mini == R){
				if(maxi == B){
					while(R){
						cout << "BR";
						if(B <= Y){
							cout << "Y";
							Y--;
						}
						B--;
						R--;
					}
					while(B){
						cout << "BY";
						B--;
					}
				}
				else{
					while(R){
						cout << "YR";
						if(Y <= B){
							cout << "B";
							B--;
						}
						Y--;
						R--;
					}
					while(B){
						cout << "YB";
						B--;
					}
				}
			}

			else if(mini == B){
				if(maxi == R){
					while(B){
						cout << "RB";
						if(R <= Y){
							cout << "Y";
							Y--;
						}
						B--;
						R--;
					}
					while(R){
						cout << "RY";
						R--;
					}
				}
				else{
					while(B){
						cout << "YB";
						if(Y <= R){
							cout << "R";
							R--;
						}
						Y--;
						B--;
					}
					while(Y){
						cout << "YR";
						Y--;
					}
				}
			}

			else{
				if(maxi == R){
					while(Y){
						cout << "RY";
						if(R <= B){
							cout << "B";
							B--;
						}
						Y--;
						R--;
					}
					while(R){
						cout << "RB";
						R--;
					}
				}
				else{
					while(Y){
						cout << "BY";
						if(B <= R){
							cout << "R";
							R--;
						}
						Y--;
						B--;
					}
					while(B){
						//cout << "BR";
						cout << "BR";
						B--;
					}
				}
			}
			cout << endl;
		}
		i++;
	}
	return 0;
}