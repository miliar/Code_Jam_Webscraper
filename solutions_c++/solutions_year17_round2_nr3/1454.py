#include<iostream>
#include<cstring>
#include<cmath>
#include<fstream>
#include<iomanip> 

#define INF 1e150 

using namespace std;

int main(){
	int T,N,Q,start[108],end[108];
	int a[108][108];
	int E[108], S[108];
	double yy[108][108];
	double sum[108];

	ifstream file1("1.in");
	ofstream file2("1.out");
	file1 >> T; file2 << setiosflags(ios::fixed);
	for (int i = 0; i < T; i++)
	{
		file1 >> N >> Q;
		for (int j = 0; j < N; j++) {
			file1 >> E[j] >> S[j];
		}
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < N; k++)
			{
				file1 >> a[j][k];
				if (j != k)
					yy[j][k] = INF;
				else
					yy[j][k] = 0;
			}
			if (j == 0)
				sum[j] = 0;
			else
				sum[j] = sum[j - 1] + a[j-1][j];
		}
		cout << "!!!" << endl;
		for (int j = 0; j < N; j++) cout << sum[j] << " ";
		cout << endl;
		for (int j = 0; j < Q; j++) {
			file1 >> start[j] >> end[j];
			start[j]--; end[j]--;
		}
		file2 << "Case #" << i + 1 << ": ";
		for (int j = 0; j < Q; j++) {
			int ss=start[j],en=end[j];
			for (int ii = 1; ii < N; ii++)
			{
				for (int jj = 0; jj < N - ii; jj++)
				{
					int kk = jj + ii; 
					if (sum[kk]-sum[jj]<=E[jj])
					    yy[jj][kk]= (sum[kk] - sum[jj])/S[jj];
					for (int ll = jj; ll <= kk; ll++)
					{
						if (yy[jj][kk]>yy[jj][ll] + yy[ll][kk])
							yy[jj][kk]=yy[jj][ll] + yy[ll][kk];
					}
				}
			}
			file2 << setprecision(6) <<yy[0][N - 1] << endl;
		}
	}
	file2.close();
	file1.close();
	return 0;
}