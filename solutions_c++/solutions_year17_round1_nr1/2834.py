#include <bits/stdc++.h>

using namespace std;

int main(){
	int t,r,c,cs=1;
	cin>>t;
	while(t--){
		cin>>r>>c;
		string mat[r];
		int chars[26];
		memset(chars,-1,sizeof(chars));
		for(int i=0;i<r;i++){
			cin>>mat[i];
		}
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(mat[i][j]!='?')
				chars[int(mat[i][j])-'A']++;
				//cout<<mat[i][j];
			}//cout<<"\n";
		}
		/*for (int i = 0; i < 26; ++i)
		{
			if(chars[i]!=-1){
				printf("%c\n",(i)+'A');
			}
		}*/
		int tlx[26],tly[26],brx[26],bry[26];
		memset(tlx,-1,sizeof(tlx));
		memset(tly,-1,sizeof(tly));
		memset(brx,-1,sizeof(brx));
		memset(bry,-1,sizeof(bry));

			for(int i=0;i<r;i++){
				for(int j=0;j<c;j++){
					if(mat[i][j]!='?'){
						brx[int(mat[i][j])-'A']=i;
						bry[int(mat[i][j])-'A']=j;
					}
				}
			}
		
			for(int i=r-1;i>=0;i--){
				for(int j=c-1;j>=0;j--){
					if(mat[i][j]!='?'){
						tlx[int(mat[i][j])-'A']=i;
						tly[int(mat[i][j])-'A']=j;
					}
				}
			}
		
		/*for (int i = 0; i < 26; ++i)
		{
			if(chars[i]!=-1){
				printf("%c %d %d %d %d\n",(i)+'A',tlx[i],tly[i],brx[i],bry[i]);
			}
		}*/
		int sum=0;
		for(int ch=0;ch<26;ch++){
			if(chars[ch]!=-1){
				for(int i=tlx[ch];i<=brx[ch];i++){
					for(int j=tly[ch];j<=bry[ch];j++){
						mat[i][j] = char(ch + 'A');
						sum++;
					}
				}
			}
		}
		int ques = (r*c)-sum;
		/*for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
		//		if(mat[i][j]!='?')
		//		chars[int(mat[i][j])-'A']++;
				cout<<mat[i][j];
			}cout<<"\n";
		}*/
	while(ques!=0){
		for(int i=0;i<r;i++){
			for(int j=1;j<c;j++){
				if(mat[i][j]=='?'){
					int ch = int(mat[i][j-1])-'A';
					if((ch+'A')!='?')
					{
						//cout<<i<<" "<<j<<" --> "<<char(ch+'A')<<"\n";
						int start = tlx[ch];
						int end = brx[ch];
						bool flag = true;
						for(int chk=start;chk<=end;chk++){
							if(mat[chk][j]!='?'){
								flag = false;
								break;
							}
						}
						if(flag){
							for(int chk=start;chk<=end;chk++){
								mat[chk][j] = mat[chk][j-1];
								bry[int(mat[chk][j]) - 'A']=j;
								ques--;
							}
						}
					}
				}
			}
		}

		/*for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
		//		if(mat[i][j]!='?')
		//		chars[int(mat[i][j])-'A']++;
				cout<<mat[i][j];
			}cout<<"\n";
		}*/

		for(int i=0;i<r;i++){
			for(int j=0;j<c-1;j++){
				if(mat[i][j]=='?'){
					int ch = int(mat[i][j+1])-'A';
					if((ch+'A')!='?')
					{
						//cout<<i<<" "<<j<<" --> "<<char(ch+'A')<<"\n";
						int start = tlx[ch];
						int end = brx[ch];
						bool flag = true;
						for(int chk=start;chk<=end;chk++){
							if(mat[chk][j]!='?'){
								flag = false;
								break;
							}
						}
						if(flag){
							for(int chk=start;chk<=end;chk++){
								mat[chk][j] = mat[chk][j+1];
								tly[(int)mat[chk][j] - 'A']=j;
								ques--;
							}	
						}
					}
				}
			}
		}

		/*for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
		//		if(mat[i][j]!='?')
		//		chars[int(mat[i][j])-'A']++;
				cout<<mat[i][j];
			}cout<<"\n";
		}*/

		for(int i=0;i<r-1;i++){
			for(int j=0;j<c;j++){
				if(mat[i][j]=='?'){
					int ch = int(mat[i+1][j])-'A';
					if((ch+'A')!='?')
					{
					//	cout<<i<<" "<<j<<" --> "<<char(ch+'A')<<"\n";
						int start = tly[ch];
						int end = bry[ch];
						bool flag = true;
						for(int chk=start;chk<=end;chk++){
							if(mat[i][chk]!='?'){
								flag = false;
								break;
							}
						}
						if(flag){
							for(int chk=start;chk<=end;chk++){
								mat[i][chk] = mat[i+1][chk];
								tlx[(int)mat[i+1][chk] - 'A']=i;
								ques--;
							}	
						}
					}
				}
			}
		}

		/*for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
		//		if(mat[i][j]!='?')
		//		chars[int(mat[i][j])-'A']++;
				cout<<mat[i][j];
			}cout<<"\n";
		}*/

		for(int i=1;i<r;i++){
			for(int j=0;j<c;j++){
				if(mat[i][j]=='?'){
					int ch = int(mat[i-1][j])-'A';
					if((ch+'A')!='?')
					{
					//	cout<<i<<" "<<j<<" --> "<<char(ch+'A')<<"\n";
						int start = tly[ch];
						int end = bry[ch];
						bool flag = true;
						for(int chk=start;chk<=end;chk++){
							if(mat[i][chk]!='?'){
								flag = false;
								break;
							}
						}
						if(flag){
							for(int chk=start;chk<=end;chk++){
								mat[i][chk] = mat[i-1][chk];
								brx[(int)mat[i-1][chk] - 'A']=i;
								ques--;
							}	
						}
					}
				}
			}
		}
	}
		cout<<"Case #"<<cs<<":"<<"\n";
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
		//		if(mat[i][j]!='?')
		//		chars[int(mat[i][j])-'A']++;
				cout<<mat[i][j];
			}cout<<"\n";
		}
		cs++;
	}
	return 0;
}