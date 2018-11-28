#include <bits/stdc++.h>

using namespace std;

#define MAX 2147483647
#define MIN -2147483647
#define clear_arr(a) memset(a,0,sizeof(a))
#define pb push_back
#define RED 0
#define ORANGE 1
#define YELLOW 2
#define GREEN 3
#define BLUE 4
#define VIOLET 5

typedef int ll;
typedef pair<ll,ll> ii;
typedef pair<double, double> dd;
typedef pair<string,string> ss;
typedef vector<ss> vss;
typedef pair<ll, ii> iii;
typedef vector<ll> vi;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef vector<string> vs;
typedef vector<ii> vii;
typedef deque<ll> dqi;
typedef unordered_set<ll> usi;
typedef set<ll> si;
typedef unordered_set<ii> usii;
typedef set<ii> sii;
typedef unordered_map<ll,ll> umii;
typedef map<ll,ll> mii; 
typedef map<string,int> msi;
typedef map<int,string> mis;

// int red, orange, yellow, green, blue, violet, 
int n;
int a[6];
int size[6];
char c[] = {'R','O','Y','G','B','V'};
vector<vi> choices;
std::vector<char> v;
bool found;
string final_result;
int count_;

void set_func(){
	vi temp = {BLUE, YELLOW, GREEN};
	choices.push_back(temp);
	vi temp1 = {BLUE};
	choices.push_back(temp1);
	vi temp2 = {RED, BLUE, VIOLET};
	choices.pb(temp2);
	vi temp3 = {RED};
	choices.push_back(temp3);
	vi temp4 = {RED, YELLOW, ORANGE};
	choices.push_back(temp4);
	vi temp5 = {YELLOW};
	choices.push_back(temp5);
}

bool check_last(){
	char xp = v[n-1];
	int index = -1;
	for(int i=0;i<6;i++)
		if(c[i] == xp){
			index = i;
			break;
		}
	if(index >= 0){
		for(int x : choices[index]){
			if(c[x] == v[0])
				return true;
		}
	}
	return false;
}

void recurse(int current, char pre){
	// printf("%d\n",++count_ );
	if(current == n ){
		if(check_last()){
			final_result = "";
			for(char xip : v)
				final_result += xip;
			found = true;
		}
		return;
	}
	if(!found){
		int index = -1;
		for(int i=0;i<6;i++)
			if(c[i] == pre){
				index = i;
				break;
			}
		if(index < 0)
			return;
		if(found)
			return;
		// printf("pre: %c\tindex : %d\tcurrent: %d\n", pre , index, current);
		int total_max = 0;
		int i=-1;
		for(int x : choices[index]){
			if(total_max < a[x]){
				total_max = a[x];
				i = x;
			}
		}
		if(i < 0)
			return;
		a[i]--;
		v[current] = c[i];
		recurse(current+1, c[i]);
		a[i]++;
	}
}



int main(){
	int cases;
	scanf("%d",&cases);
	
	set_func();
	for(int xl=1;xl<=cases;xl++){
		int count_ = 0;
		found = false;
		// scanf("%d %d %d %d %d %d %d", &n, &red, &orange, &yellow, &green, &blue, &violet);
		scanf("%d",&n);
		for(int i=0;i<6;i++)
			scanf("%d",&a[i]);
		v.assign(n, 'x');
		int index = -1;
		int max_found = -1;
		for(int i=0;i<6;i++){
			if(a[i] > max_found){
				max_found = a[i];
				index = i;
			}
		}
		// printf("index: %c\n",c[index] );
		// recurse(1, c[index]);
		for(int i=0;i<6;i++){
			if(a[i] > 0 and !found){
				v[0] = c[i];
				a[i]--;
				recurse(1,c[i]);
				a[i]++;
			}
		}
		printf("Case #%d: ", xl);
		if(found){
			// for(char cp : v){
			// 	printf("%c",cp );
			// }
			printf("%s\n", final_result.c_str());
		}else{
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}