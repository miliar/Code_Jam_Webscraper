#include <vector>
#include <utility>
#include <iostream>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> taken;

vvi row;
taken occu;
int n, k;


void update(int pos){
	for(int i=pos-1; i>0; --i){
		if(!occu[i]){
			row[i][3]=pos-i-1;
			row[i][0]=min(row[i][2], row[i][3]); 
			row[i][1]=max(row[i][2], row[i][3]);		
		}else{
			break;
		}
	}
	for(int i=pos+1; i<n+1; ++i){
		if(!occu[i]){
			row[i][2]=i-pos-1;
			row[i][0]=min(row[i][2], row[i][3]); 
			row[i][1]=max(row[i][2], row[i][3]);		
		}else{
			break;
		}
	}
}

void mark(int pos){
	occu[pos]=1;
	row[pos]=vi(4, 0);
	update(pos);
}

void fill(){
	row.assign(n+2, vi(4, 0));
	occu.assign(n+2, 0);
	occu[0]=1;
	occu[n+1]=1;
	for(int i=1; i<n+1; ++i){
		int ls=i-1, rs=n-i;
		row[i][0]=min(ls, rs); 
		row[i][1]=max(ls, rs);
		row[i][2]=ls;
		row[i][3]=rs;
	}
}

int addto2(){
	vi minPos, maxPos;
	int maxMin=0, maxMax=0;
	for(int i=1; i<n+1; ++i){
		if(row[i][0]>maxMin){
			maxMin=row[i][0];
		}
	}
	for(int i=1; i<n+1; ++i){
		if(row[i][0]==maxMin){
			minPos.push_back(i);
		}
	}
	if(minPos.size()==1){
		return minPos[0];
	}else{
		for(auto it=minPos.begin(); it!=minPos.end(); ++it){
			if(row[*it][1]>maxMax){
				maxMax=row[*it][1];
			}
		}
		for(auto it=minPos.begin(); it!=minPos.end(); ++it){
			if(row[*it][1]==maxMax){
				maxPos.push_back(*it);
			}
		}
		return maxPos[0];
	}
}


void addto(){
	vi minPos, maxPos;
	int maxMin=0, maxMax=0;
	for(int i=1; i<n+1; ++i){
		if(row[i][0]>maxMin){
			maxMin=row[i][0];
		}
	}
	for(int i=1; i<n+1; ++i){
		if(row[i][0]==maxMin){
			minPos.push_back(i);
		}
	}
	if(minPos.size()==1){
		mark(minPos[0]);
	}else{
		for(auto it=minPos.begin(); it!=minPos.end(); ++it){
			if(row[*it][1]>maxMax){
				maxMax=row[*it][1];
			}
		}
		for(auto it=minPos.begin(); it!=minPos.end(); ++it){
			if(row[*it][1]==maxMax){
				maxPos.push_back(*it);
			}
		}
		mark(maxPos[0]);
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	int tc=0;
	cin>>tc;
	for(int i=1; i<=tc; ++i){
		cin>>n>>k;
		fill();
		for(int j=1; j<k; ++j){
			addto();
		}
		int ans=addto2();		
		cout<<"Case #"<<i<<": "<<row[ans][1]<<' '<<row[ans][0]<<endl;
	}
	return 0;
}








