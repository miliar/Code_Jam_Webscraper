#include <bits/stdc++.h>

using namespace std;

#define FILENAME "B-large"

template <typename T1, typename T2, typename T3> class trio { public: T1 a; T2 b; T3 c; };

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<char> vc;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<ll, ll> pl4;
typedef trio<int, int, int> tiii;
typedef vector<pii*> vpii;
typedef vector<pii*> vpl4;
typedef vector<tiii*> vtiii;
typedef vector<vi*> graph;
typedef vector<vpii*> wgraph;
typedef unordered_map<int, int> mii;
typedef unordered_map<char, int> mci;
typedef unordered_map<string, int> msi;
typedef unordered_map<int, string> mis;
typedef unordered_map<string, ll> msll;
typedef unordered_map<string, string> mss;
typedef unordered_map<int, int> mii;
typedef unordered_map<ll, ll> ml4;
typedef deque<int> qi;
typedef deque<char> qc;

#define inf 1e8
#define For(i,n) for(int i = 0; i < int(n); i++)
#define For1(i,n) for(int i = 1; i <= int(n); i++)
#define Forbe(i,begin,end) for(int i = int(begin); i < int(end); i++)
#define fit(it,o) for(auto it = (o)->begin(); it != (o)->end(); it++)
#define echo(txt) cout << txt << endl
#define pb(x) push_back(x)
#define op operator
#define sof(M) (sizeof(M)/sizeof(*M))
#define show(v) For(FV1,(v)->size()){ cout << FV1 << ": " << (v)->op[](FV1) << endl; }
#define show2(v) For(FV1,(v)->size()){ cout << (v)->op[](FV1) << " "; }
#define show2_vpii(v) For(FV1,(v)->size()){ cout << (v)->op[](FV1)->first << "," << (v)->op[](FV1)->second << " "; }
#define show_graph(g) For1(FV2,(g)->size()-1){ cout << FV2 << ": "; show2((g)->op[](FV2)); cout << endl; }
#define show_wgraph(g) For1(FV2,(g)->size()-1){ cout << FV2 << ": "; show2_vpii((g)->op[](FV2)); cout << endl; }
#define show_matrix(M) For(FV1,sof(M)){ For(FV2,sof((M)[FV1])){ cout << (M)[FV1][FV2] << " "; } cout << endl; }
#define m unordered_map
#define mfind(map, key) ((map)->find(key) != (map)->end())
#define Sort(v) sort((v)->begin(), (v)->end())
#define rev(v) reverse((v)->begin(),(v)->end())
#define pause cin.ignore()

struct pii_comp { bool op()(pii* p1, pii* p2){ if(p2->second < p1->second){ return true; } else { return false; }}};
struct tiii_comp { bool op()(tiii* t1, tiii* t2){ if(t2->c < t1->c){ return true; } else { return false; }}};
typedef priority_queue<int> hi;
typedef priority_queue<pii, vpii, pii_comp> hpii;
typedef priority_queue<tiii, vtiii, tiii_comp> htiii;

int ctoi(char c){ return ((int)c) - 48; }

/*-----------------------------------------------------------------------------------------------------*/

int main(){
	
	string input_file = FILENAME;
	input_file += ".in";
	
	string output_file = FILENAME;
	output_file += ".out";
	ofstream os;
	os.open(output_file);
	
	ifstream is(input_file);
	if( is.is_open() ){
		
		ll T;
		is >> T;
		
		vs v;
		
		For(i,T){
			
			string str;
			is >> str;
			v.pb(str);
		}
		
		For(i,T){
			
			bool tidy = false;
			string last_tidy;
			string s = v[i];
			
			while(tidy == false){
				
				last_tidy = "";
				tidy = true;
				
				For(j,s.size()){
					
					if(j == (int)s.size()-1){ last_tidy += s[j]; continue; }
					
					if(ctoi(s[j]) > ctoi(s[j+1])){
						
						last_tidy += to_string(ctoi(s[j])-1);
						Forbe(k,j+1,s.size()){
							
							last_tidy += to_string(9);
						}
						
						tidy = false;
						break;
					}
					else { last_tidy += s[j]; }
				}
				
				if(ctoi(last_tidy.front()) == 0){ last_tidy.erase(last_tidy.begin()); tidy = false; }
				s = last_tidy;
			}
			
			os << "Case #" << i+1 << ": ";
			os << last_tidy << endl;
		}
		
		is.close();
	}
	else { cout << "Unable to open file"; }
	
	os.close();
	return 0;
}
