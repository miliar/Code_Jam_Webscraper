
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <climits>

#define ll long long

using namespace std;

int main(){
	int t;
	cin>>t;
	int a=0;
	while (t--){
		a++;
		cout<<"Case #"<<a<<": ";

		int c1,c2;
		cin>>c1>>c2;
		vector<pair<int,pair<int,int> > > input;
		int ans=0;

		for (int i=0;i<c1;i++){
			int s,e;
			cin>>s>>e;
			input.push_back(make_pair(s,make_pair(e,0)));
		}

		for (int i=0;i<c2;i++){
			int s,e;
			cin>>s>>e;
			input.push_back(make_pair(s,make_pair(e,1)));
		}

		sort(input.begin(),input.end());
		int t1=0,t2=0;
		for (int i=0;i<input.size();i++){
			if (input[i].second.second==0){
				t1+=input[i].second.first-input[i].first;
				if (i!=input.size()-1){
					if (input[i+1].second.second==0){
						t1+=input[i+1].first-input[i].second.first;
					}
					else{
						ans++;
					}
				}
			}
			else{
				t2+=input[i].second.first-input[i].first;
				if (i!=input.size()-1){
					if (input[i+1].second.second==1){
						t2+=input[i+1].first-input[i].second.first;
					}
					else{
						ans++;
					}
				}
			}
		}

		if (input[0].second.second==input[c1+c2-1].second.second){
			if (input[0].second.second==0){
				t1+=input[0].first;
				t1+=1440-input[c1+c2-1].second.first;
			}
			else{
				t2+=input[0].first;
				t2+=1440-input[c1+c2-1].second.first;

			}
		}
		else{
			ans++;
		}
		//cout<<t1<<" "<<t2<<endl;



		if ((t1<720 && t2<=720) || (t2<720&& t1<=720) || (t1==720 && t2==720)){
			cout<<ans<<endl;
				// vector<int> blocks;
				// for (int i=0;i<input.size()-1;i++){
				// 	if (input[i].second.second!=input[i+1].second.second){
				// 		blocks.push_back(input[i+1].first-input[i].second.first);
				// 	}

				// }
				// if (input[0].second.second!=input[c1+c2-1].second.second){
				// 	blocks.push_back(input[i+1].first-input[i].second.first);
				// }
				// int temp=t1;
				// if(input[0].second.second==1){
				// 	temp=t2;
				// }
				// for (int i=0;i<blocks.size();i++){
				// 	if (temp+blocks[i]>=720){
				// 		ans
				// 	}
				// }

		}
		else{
			
			vector<int> blocks1;
			vector<int> blocks2;
			for (int i=0;i<input.size()-1;i++){
				if (input[i].second.second==input[i+1].second.second){
					if (input[i].second.second==0){
						blocks1.push_back(input[i+1].first-input[i].second.first);
					}
					else{
						blocks2.push_back(input[i+1].first-input[i].second.first);

					}
				}
			}
			if (input[0].second.second==input[c1+c2-1].second.second){
				if (input[0].second.second==0){
					blocks1.push_back(input[0].first+1440-input[c1+c2-1].second.first);
				}
				else{
					blocks2.push_back(input[0].first+1440-input[c1+c2-1].second.first);

				}
			}

			// cout<<blocks1.size();
			// for (int i=0;i<blocks1.size();i++){
			// 	cout<<blocks1[i]<<" ";
			// }
			// cout<<endl;
			if (t1>720){
				int extra=t1-720;
				sort(blocks1.begin(),blocks1.end());
				for (int i=blocks1.size()-1;i>=0;i--){
					if (blocks1[i]<extra){
						ans+=2;
						extra-=blocks1[i];
					}
					else{
						ans+=2;
						break;
					}
				}

			}
			else{
				int extra=t2-720;
				sort(blocks2.begin(),blocks2.end());
				for (int i=blocks2.size()-1;i>=0;i--){
					if (blocks2[i]<extra){
						ans+=2;
						extra-=blocks2[i];
					}
					else{
						ans+=2;
						break;
					}
				}

			}
			cout<<ans<<endl;

		}

		// My code



	}

	return 0;
}

