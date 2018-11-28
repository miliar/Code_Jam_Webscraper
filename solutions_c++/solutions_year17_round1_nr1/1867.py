#include<iostream>

using namespace std;

int main(){
	
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;

	cin>>t;
	int z=t;
	while(t--){
		int r,c;

		cin>>r>>c;

		char arr[r][c];

		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cin>>arr[i][j];
			}
		}

		int count_filled_row = 0;
		int flag_nonempty_row = 0;

		for(int i=0;i<r;i++){
			flag_nonempty_row = 0;
			for(int j=0;j<c;j++){
				if(flag_nonempty_row == 0 && arr[i][j]!='?'){
					flag_nonempty_row=1;
					count_filled_row++;
					if(j>0){
						for(int k = j-1;k>=0;k--)
							arr[i][k]=arr[i][j];
					}

				}

				if(flag_nonempty_row==1 && arr[i][j]=='?'){
					arr[i][j]=arr[i][j-1];
				}

			}

			if(count_filled_row==1 && i>0 && flag_nonempty_row==1){
				for(int k=i-1;k>=0;k--){
					for(int j=0;j<c;j++){
						arr[k][j]=arr[i][j];
					}
					count_filled_row++;
				}
			}

			if(flag_nonempty_row==0 && count_filled_row>0){
				for(int j=0;j<c;j++){
					arr[i][j]=arr[i-1][j];
				}
			}
		}
		
		cout<<"Case #"<<z-t<<": "<<endl;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cout<<arr[i][j];
			}
			cout<<endl;
		}
	}
}
