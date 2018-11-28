#include<fstream>
#include<vector>
#include<algorithm>
#include<queue>
#include<stack>
#include<math.h>
using namespace std;

ifstream cin ("B-large.in");
ofstream cout ("ax2.out");

int ca =0;

void doit(){
	ca++;
	int c,j;
	int a,b;
	
	int cl = 720;
	int jl = 720;
	
	vector < pair < int , pair < int , char > > > gmt;
	//durr , end pou en na girepso , arki pou en na girepso gia na kamo sixonefsi
	vector < pair < int , pair < int , int > > > cint;//kena pou prepi na gemosoume me cameron
	vector < pair < int , pair < int , int > > > jint;//kena p p n g me jaime
	
	cin>>c>>j;
	
	for(int i=0;i<c;i++){
		cin>>a>>b;
		gmt.push_back(make_pair(a, make_pair(b,'j')  ));
		jl = jl - (b-a);
	}
	
	for(int i=0;i<j;i++){
		cin>>a>>b;
		gmt.push_back(make_pair(a, make_pair(b,'c')  ));
		cl = cl - (b-a);
	}
	
	if(gmt.size()==0){
		cout<<"Case #"<<ca<<": "<<2<<endl;
		return;
	}
	
	if(gmt.size()==1){
		cout<<"Case #"<<ca<<": "<<2<<endl;
		return;
	}
	
	bool lastconn = false;
	
	sort(gmt.begin(),gmt.end());
	
	for(int i=0;i<gmt.size();i++){
		if(i==gmt.size()-1){
			// an ine to telefteo thoro to proto !!!!!
			if(gmt[i].second.second == gmt[0].second.second){
				if(gmt[i].second.second == 'j'){
					jint.push_back(make_pair( gmt[0].first + (1440 - gmt[i].second.first), make_pair( gmt[i].second.first , gmt[0].first) ));
				}
				if(gmt[i].second.second == 'c'){
					cint.push_back(make_pair( gmt[0].first + (1440 - gmt[i].second.first), make_pair( gmt[i].second.first , gmt[0].first) ));
				}
			}
			else{
				// dont care
			}
		}
		else{
			if(gmt[i].second.second == gmt[i+1].second.second){
				if(gmt[i].second.second == 'j'){
					jint.push_back(make_pair( gmt[i+1].first - gmt[i].second.first , make_pair( gmt[i].second.first , gmt[i+1].first) ));
				}
				if(gmt[i].second.second == 'c'){
					cint.push_back(make_pair( gmt[i+1].first - gmt[i].second.first , make_pair( gmt[i].second.first , gmt[i+1].first) ));
				}
			}
			else{
				// dont care
			}
		}
	}
	
	sort(cint.begin(),cint.end());
	sort(jint.begin(),jint.end());	
	
	for(int i=0;( ( i<cint.size()) &&  ( cl >= cint[i].first ) );i++){
		// mporume na to kamoume ara pame
		cl = cl - cint[i].first;
		for(int j=0;j<gmt.size();j++){ //en na enosoume ta thkio ta intervals
			if(j==gmt.size()-1){//an ine to telefteo
				if(cint[i].second.first == gmt[j].second.first){
					lastconn = true;
				}
			}
			else{// an ine to opiodipote
				if(cint[i].second.first == gmt[j].second.first){
					//ivra to prepi na to enoso me to epomeno
					gmt[j+1].first = gmt[j].first;
					gmt.erase(gmt.begin()+j);
					break;	
				}
			}
		}
	}
	
	for(int i=0;( ( i<jint.size()) &&  ( jl >= jint[i].first ) );i++){
		// mporume na to kamoume ara pame
		jl = jl - jint[i].first;
		for(int j=0;j<gmt.size();j++){ //en na enosoume ta thkio ta intervals
			if(j==gmt.size()-1){//an ine to telefteo
				if(jint[i].second.first == gmt[j].second.first){
					lastconn = true;
				}
			}
			else{// an ine to opiodipote
				if(jint[i].second.first == gmt[j].second.first){
					//ivra to prepi na to enoso me to epomeno
					gmt[j+1].first = gmt[j].first;
					gmt.erase(gmt.begin()+j);
					break;	
				}
			}
		}
	}
	
	if(lastconn){//aferoume ena
		int count = 0;
		for(int i=0;i<gmt.size()-1;i++){
			if(gmt[i].second.second == gmt[i+1].second.second){
				count = count + 2;
			}
			else{
				count = count + 1;
			}	
		}
		cout<<"Case #"<<ca<<": "<<count<<endl;
	}
	else{
		int count = 0;
		for(int i=0;i<gmt.size();i++){
			if(i!=gmt.size()-1){
				if(gmt[i].second.second == gmt[i+1].second.second){
					count = count + 2;
				}
				else{
					count = count + 1;
				}	
			}
			else{
				if(gmt[i].second.second == gmt[0].second.second){
					count = count + 2;
				}
				else{
					count = count + 1;
				}	
			}
		}	
		cout<<"Case #"<<ca<<": "<<count<<endl;
	}
}

int main(){
	
	int t;
	cin>>t;
	while(t--){
		doit();
	}
	
}
