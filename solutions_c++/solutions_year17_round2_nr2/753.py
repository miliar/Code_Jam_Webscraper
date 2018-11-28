#include <vector>
#include <iostream>

using namespace std;


bool test0(int R2, int B2, int Y2)
{
	return !(R2 + B2 < Y2 || B2 + Y2 < R2 || Y2 + R2 < B2);
}


string solve(int R, char cR, int B, char cB, int Y, char cY)
{
	if(R < B)
		return solve(B, cB, R, cR, Y, cY);
	if(R < Y)
		return solve(Y, cY, R, cR, B, cB);
	if(B < Y)
		return solve(R, cR, Y, cY, B, cB);
	
	
	int d = B + Y - R;
	
	string s;
	for(int i = 0; i < Y; i++){
		s.push_back(cR);
		s.push_back(cY);
		if(i < d)
			s.push_back(cB);
	}
	for(int i = 0; i < B - d; i++){
		s.push_back(cR);
		s.push_back(cB);
	}
		
	return s;
}


int main()
{	
	int T;
	cin >> T;
	
	for(int i = 1; i <= T; i++)
	{
		cout << "Case #" << i << ": ";
	
		int N;
		cin >> N;
		int R,O,Y,G,B,V;
		cin >> R >> O >> Y >> G >> B >> V;

		int R2 = R;
		int B2 = B;
		int Y2 = Y;

		if(O != 0){
			if(B < O
				|| (B == O && (V != 0 || R != 0 || Y != 0 || G != 0))
			){
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			B2 = B - O;
			
		}
		
		if(G != 0){
			if(R < G
				|| (R == G && (V != 0 || B != 0 || Y != 0 || O != 0))
			){
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			R2 = R - G;
		}

		if(V != 0){
			if(Y < V
				|| (Y == V && (B != 0 || R != 0 || O != 0 || G != 0))
			){
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			Y2 = Y - V;
		}

		
		if(R2 + B2 < Y2 || B2 + Y2 < R2 || Y2 + R2 < B2){
			cout << "IMPOSSIBLE" << endl;
			continue;
		}


		string s = solve(R2, 'R', B2, 'B', Y2, 'Y');

		if(R == G && R != 0){
			for(int i = 0; i < R; i++){
				s.push_back('R');
				s.push_back('G');
			}
		}		
		else if(B == O && B != 0){
			for(int i = 0; i < B; i++){
				s.push_back('B');
				s.push_back('O');
			}
		}		
		else if(Y == V && Y != 0){
			for(int i = 0; i < Y; i++){
				s.push_back('Y');
				s.push_back('V');
			}
		}
		else {
			if(G != 0){
				string t;
				bool found = false;
				for(int i = 0; i < s.size(); i++){
					t.push_back(s[i]);
					if(s[i] == 'R' && !found){
						found = true;
						for(int j = 0; j < G; j++){
							t.push_back('G');
							t.push_back('R');
						}
					}
				}
				s = t;
			}

			if(V != 0){
				string t;
				bool found = false;
				for(int i = 0; i < s.size(); i++){
					t.push_back(s[i]);
					if(s[i] == 'Y' && !found){
						found = true;
						for(int j = 0; j < V; j++){
							t.push_back('V');
							t.push_back('Y');
						}
					}
				}
				s = t;
			}

			if(O != 0){
				string t;
				bool found = false;
				for(int i = 0; i < s.size(); i++){
					t.push_back(s[i]);
					if(s[i] == 'B' && !found){
						found = true;
						for(int j = 0; j < O; j++){
							t.push_back('O');
							t.push_back('B');
						}
					}
				}
				s = t;
			}
		}

		cout << s << endl;
	}
}
