#include<map> 
#include<set>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

int main(){

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int n,r,o,y,g,b,v,p1,p2,p3;
	string s1,s2,s3;

	int ntc;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> n;
		cin >> r >> o >> y >> g >> b >> v;
		cout << "Case #" << tc << ": ";
		if ((o>0 && b<=o) || (g>0 && r<=g) || (v>0 && y<=v)){
			if (o>0 && o==b){
				int k = o;
				o = b = 0;
				if (o>0 || b>0 || g>0 || r>0 || v>0 || y>0)
					cout << "IMPOSSIBLE" << endl;
				else{
					for (int i=0;i<k;i++)
						cout << "OB";
					cout << endl;
				}
			}
			else
			if (g>0 && g==r){
				int k = g;
				g = r = 0;
				if (o>0 || b>0 || g>0 || r>0 || v>0 || y>0)
					cout << "IMPOSSIBLE" << endl;
				else{
					for (int i=0;i<k;i++)
						cout << "GR";
					cout << endl;
				}
			}
			else
			if (v>0 && v==y){
				int k = v;
				v = y = 0;
				if (o>0 || b>0 || g>0 || r>0 || v>0 || y>0)
					cout << "IMPOSSIBLE" << endl;
				else{
					for (int i=0;i<k;i++)
						cout << "VY";
					cout << endl;
				}
			}
			else
				cout << "IMPOSSIBLE" << endl;
		}
		else{
			b -= o;
			r -= g;
			y -= v;
			vector<pair<int,string> > num;
			num.push_back(make_pair(r,"R"));
			num.push_back(make_pair(b,"B"));
			num.push_back(make_pair(y,"Y"));
			sort(num.begin(),num.end());
			p1 = num[2].first-num[1].first;
			p2 = num[1].first-num[0].first;
			p3 = num[0].first-p1;
			if (p1<0 || p2<0 || p3<0)
				cout << "IMPOSSIBLE" << endl;
			else{
				s1 = num[0].second+num[2].second+num[1].second+num[2].second;
				s2 = num[1].second+num[2].second;
				s3 = num[0].second+num[1].second+num[2].second;
				string res = "";
				string rest = "";
				for (int i=0;i<p1;i++) res+=s1;
				for (int i=0;i<p3;i++) res+=s3;
				for (int i=0;i<p2;i++) res+=s2;

				for (int i=0;i<res.length();i++){
					if (res[i]=='B'){
						if (o>0){
							for (int k=0;k<o;k++)
								rest+="BO";
						}
						rest+="B";
						o = 0;
					}
					else
					if (res[i]=='R'){
						if (g>0){
							for (int k=0;k<g;k++)
								rest+="RG";
							g = 0;
						}
						rest+="R";
					}
					else
					if (res[i]=='Y'){
						if (v>0){
							for (int k=0;k<v;k++)
								rest+="YV";
							v = 0;
						}
						rest+="Y";
					}
				}

				cout << rest << endl;
			}
		}
	}

	return 0;
}