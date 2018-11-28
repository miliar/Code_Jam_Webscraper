#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

// if(!did){
// 	for (int r = i+1; r < R; r++) // to the right
// 	{
// 		if (mat[r][j] == '?'){
// 			mat[r][j] = mat[i][j];
// 			did = true;
// 		}
// 		else
// 			break;
// 	}

// 	for (int r = i-1; r >= 0; r--) // to the right
// 	{
// 		if (mat[r][j] == '?'){
// 			mat[r][j] = mat[i][j];
// 			did = true;
// 		}
// 		else
// 			break;
// 	}
// }
// 
vector<string> flip(vector<string> &ss, int R, int C){
	std::vector<string> ff;
	for (int i = 0; i < C; ++i)
	{
		string s = "";
		for (int j = 0; j < R; ++j)
		{
			s += ss[j][i];
		}
		ff.push_back(s);
	}
	return ff;
}
void testcase(int ncase, vector<string> &mat, int R, int C ){
	cout << "Case #" << ncase << ":" << endl;

	// for (int i = 0; i < R; ++i)
	// {
	// 	for (int j = 0; j < C; ++j)
	// 	{
	// 		cout << mat[i][j];
	// 	}
	// 	cout << endl;
	// }
	for (int i = 0; i < R; ++i)
	{
		for (int j = 0; j < C; ++j)
		{
			bool did = false;
			if (mat[i][j] != '?'){
				if(!did){
					for (int r = j-1; r >= 0; r--) // to the left
					{
						if (mat[i][r] == '?'){
							mat[i][r] = mat[i][j];
							did = true;
						}
						else
							break;
					}
				
					for (int r = j+1; r < C; r++) // to the right
					{
						if (mat[i][r] == '?'){
							mat[i][r] = mat[i][j];
							did = true;
						}
						else
							break;
					}
				}
				
			}
		}
	}
	mat = flip(mat, R, C);
	swap(R,C);
	// for (int i = 0; i < R; ++i)
	// {
	// 	for (int j = 0; j < C; ++j)
	// 	{
	// 		cout << mat[i][j];
	// 	}
	// 	cout << endl;
	// }
	for (int i = 0; i < R; ++i)
	{
		for (int j = 0; j < C; ++j)
		{
			bool did = false;
			if (mat[i][j] != '?'){
				if(!did){
					for (int r = j-1; r >= 0; r--) // to the left
					{
						if (mat[i][r] == '?'){
							mat[i][r] = mat[i][j];
							did = true;
						}
						else
							break;
					}
				
					for (int r = j+1; r < C; r++) // to the right
					{
						if (mat[i][r] == '?'){
							mat[i][r] = mat[i][j];
							did = true;
						}
						else
							break;
					}
				}
				
			}
		}
	}
	mat = flip(mat, R, C);
	swap(R,C);
	for (int i = 0; i < R; ++i)
	{
		for (int j = 0; j < C; ++j)
		{
			cout << mat[i][j];
		}
		cout << endl;
	}

}

int main(){
	int T;

	cin >> T;
	
	vector<string> mat;
	int r,c;
	string aa;
	for (int i = 0; i < T; ++i)
	{
		mat.clear();
		cin >> r >> c;
		for (int j = 0; j < r; ++j)
		{
			cin >> aa;
			mat.push_back(aa);
		}
		testcase(i+1, mat, r, c);
	}

	return 0;
}