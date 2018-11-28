#include<iostream>
#include<fstream>
#include<vector>
#include<utility>
#include<algorithm>
#define ull unsigned long long
#define vit vector<bool>::iterator
using namespace std;
bool isemp(bool i){
	return !i;
}
bool ismax(pair<int,int> p1,pair<int,int> p2){
	return p1.first<p2.first;
}
int main(void){
	
	freopen("small_input.txt", "r", stdin);
	freopen("small_output.txt", "w", stdout);
	
	int T; cin>>T;
	for(int t=1;t<=T;t++){
		ull n,k; cin>>n>>k;
		cout<<"Case #"<<t<<": ";
		//cout<<'\n';
		vector<bool> v(n,0);
		//v[1]=1;
		for(int i=0;i<k;i++){
			vector<int> mne(n);
			vector<int> mxe(n);
			int minv,maxv,maxf;
			for(int j=0;j<n;j++){
				if(!v[j]){
					vit vls=v.begin();
					vit vrs=v.end();
					for(int k=j-1;k>=0;k--)
						if(v[k]==1){
							vls=v.begin()+k;
							break;
						}
					for(int k=j+1;k<n;k++)
						if(v[k]==1){
							vrs=v.begin()+k;
							break;
						}
					int ls;
					if(j==0) ls=0;
					else ls=count_if(vls,v.begin()+j,isemp);
					int rs=count_if(v.begin()+j+1,vrs,isemp);
					//cout<<"j "<<j<<" l "<<ls<<" r "<<rs;
					mne[j]=min(ls,rs);
					mxe[j]=max(ls,rs);
					//cout<<" minv "<<mne[j]<<" maxv "<<mxe[j]<<'\n';
				}
			}
			/*cout<<"\nmne v ";
			for(auto it=mne.begin();it!=mne.end();it++) cout<<(*it)<<' ';
			cout<<'\n';*/
			auto mn=max_element(mne.begin(),mne.end());
			auto mx=max_element(mxe.begin(),mxe.end());
			minv=*mn;
			maxv=*mx;
			//cout<<minv<<' '<<maxv;
			
			int cmn=count(mne.begin(),mne.end(),*mn);
			//cout<<" cmn "<<cmn<<'\n';
			/*
			cout<<" minv ";
			for(int j=0;j<n;j++) cout<<(*(mne.begin()+j));
			cout<<'\n';
			*/
			if(cmn==1) {
				int mnin=mn-mne.begin();
				//cout<<"occ "<<mnin<<'\n';
				v[mnin]=1;
				maxf=mxe[mnin];
				//cout<<" maxf "<<maxf<<'\n';
			}
			else{
				vector< pair<int,int> > mnmx;
				for(int j=0;j<n;j++){
					//cout<<"j "<<j<<" minv "<<(*(mne.begin()+j))<<'\n';
					if(!v[j]){
						if(mne[j]==minv){
							mnmx.push_back(make_pair(mxe[j],j));
							//cout<<"mnmx j "<<j<<" mxe "<<mxe[j]<<'\n';
						}
					}
						
				}
				auto mnx=max_element(mnmx.begin(),mnmx.end(),ismax);
				//cout<<"occ "<< mnx->second;
				v[mnx->second]=1;
				maxf=mnx->first;
				//cout<<" maxf "<<maxf<<'\n';
			}
			if(i==k-1)
				cout<<maxf<<' '<<minv;
		}
		cout<<'\n';
	}
	return 0;
}
