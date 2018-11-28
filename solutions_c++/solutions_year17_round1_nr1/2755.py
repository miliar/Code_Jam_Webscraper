#include <iostream>
#include <cstring>
using namespace std;


int T = 0, t = 0, r, c;
char S[30][30];
int min_i[30], min_j[30];
int max_i[30], max_j[30];
int main(){
	//freopen("codejam01_in.txt", "r", stdin);
	//freopen("codejam01_out.txt", "w", stdout);
	cin>>T;
	while(t++ < T){

		for(int i = 0;i<30;i++)
			min_i[i] = 100;
		for(int i = 0;i<30;i++)
			min_j[i] = 100;
		for(int i = 0;i<30;i++)
			max_i[i] = -1;
		for(int i = 0;i<30;i++)
			max_j[i] = -1;
		cin>>r>>c;

		for(int i = 0;i< r;i++){
			cin>>S[i];
		}

		for(int i = 0;i< r;i++){
			for(int j = 0;j<c;j++){
				if(S[i][j] == '?'){
					continue;
				}
				if(min_i[S[i][j]-'A']>i)
					min_i[S[i][j]-'A'] = i;
				if(min_j[S[i][j]-'A']>j)
					min_j[S[i][j]-'A'] = j;
				if(max_i[S[i][j]-'A']<i)
					max_i[S[i][j]-'A'] = i;
				if(max_j[S[i][j]-'A']<j)
					max_j[S[i][j]-'A'] = j;
			}
		}

		for(int k = 0;k<26;k++){
			//cout<<min_i[k]<<" "<<min_j[k]<<" "<<max_i[k]<<" "<<max_j[k]<<endl;
			for(int m = min_i[k]; m<=max_i[k]; m++){
				for(int n = min_j[k]; n<=max_j[k]; n++){
					S[m][n] = 'A'+k;
				}
			}
		}


		for(int i = 0;i<r;i++){
			for(int j = 0;j<c;j++){
				if(S[i][j]!='?')
					continue;

				for(int k = 0;k<26;k++){
					if(min_i[k] == 100) continue;
					int n_i, n_j, m_i, m_j;
					n_i = min_i[k]<i?min_i[k]:i;
					n_j = min_j[k]<j?min_j[k]:j;
					m_i = max_i[k]>i?max_i[k]:i;
					m_j = max_j[k]>j?max_j[k]:j;
					int flag = 1;
					for(int m = n_i; m<=m_i; m++){
						for(int n = n_j; n<=m_j; n++){
							if(S[m][n]!='A'+k && S[m][n]!='?'){
								flag = 0;
								break;
							}
							if(!flag)
								break;
						}
					}
					if(flag){
						for(int m = n_i; m<=m_i; m++){
							for(int n = n_j; n<=m_j; n++){
								S[m][n] = 'A'+k;
							}
						}
						min_i[k] = n_i;
						min_j[k] = n_j;
						max_i[k] = m_i;
						max_j[k] = m_j;
					}

				}

			}
		}

		printf("Case #%d:\n",t);
		for(int i = 0;i< r;i++){
			cout<<S[i]<<endl;
		}

		
	}
	return 0;
}