#include<iostream>
#include<vector>
#include<algorithm>
#include<numeric>


using namespace std;

int64_t vec2num(vector<int64_t> &vec){
	int64_t num=0;
	for(int64_t n : vec){
		num=num*10+n;
	}
	
	return num;
}

vector<int64_t> num2vec(int64_t i){
	vector<int64_t> vec;
	while(i>0){
		vec.push_back(i%10);
		i/=10;
	}
	reverse(vec.begin(),vec.end());
	
	return vec;
}

vector<int64_t> num2vec(vector<int64_t> vec){
    
	 
	
	
	return vec;
}



int main(void){
	int T=0;
	int64_t N;
	
	cin>>T;
	for(int ii=0;ii<T ; ii++){
		cin >> N;
		vector<int64_t> cnum=num2vec(N);
		
		
		bool change=false;
		for(int kk=0;kk<cnum.size();kk++)	{
			change=false;
		
			int jj=0;
			for(jj=0;jj<cnum.size()-1;jj++){
				if(cnum[jj]>cnum[jj+1]){
					cnum[jj]=cnum[jj]-1;
					change=true;
					break;
				}
			}
			if(change){
				jj++;
				while(jj<cnum.size()){
					cnum[jj]=9;
					jj++;
				}
			}
			
		    if(!change) break;
		
		}
		
		int64_t nnum=vec2num(cnum);
		
		cout<<"Case #"<<ii+1<<": "<<nnum<<endl;
		
	}
	
	return 0;
}
