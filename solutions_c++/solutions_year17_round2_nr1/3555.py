#include "pancakes.hpp"

using namespace std;

inline void ln(){putchar('\n');};
inline void space(){putchar(' ');};

inline void scan(int& a){ scanf("%d",&a); };
inline void scan (long int &a){scanf("%ld",&a);};
inline void scan (long long int &a){scanf("%lld",&a);};
inline void scan (string& s){ //stop at the end of the line
	int c;
	while((c=getchar())=='\n'||c==' '||c=='\r');
	do{
		switch(c){
		case'\n':case'\r':return;
		default:s+=c;
		}
	}while((c=getchar())!=EOF);
};
inline void scanspace (string& s){ //stop when encountering a space
	int c;
	while((c=getchar())=='\n'||c==' '||c=='\r');
	do{
		switch(c){
		case'\n':case'\r': case' ':return;
		default:s+=c;
		}
	}while((c=getchar())!=EOF);
};
inline void scan (char& c){ while((c=getchar())=='\n'||c==' '||c=='\r');};
inline void scan (double& a){scanf("%lf",&a);};
inline void scan (vector<int > &v, int n){
	int tmp;
	for(int i=0;i<n;i++){
		scan(tmp);
		v.push_back(tmp);
	}
};
inline void scan (vector<long int> &v, int n){
	long int tmp;
	for(int i=0;i<n;i++){
		scan(tmp);
		v.push_back(tmp);
	}
};
inline void scan (vector<long long int> &v, int n){
	long long int tmp;
	for(int i=0;i<n;i++){
		scan(tmp);
		v.push_back(tmp);
	}
};
inline void scan (vector<double> &v, int n){
	double tmp;
	for(int i=0;i<n;i++){
		scan(tmp);
		v.push_back(tmp);
	}
};
inline void scan (vector<char> &v, int n){
	char tmp;
	for(int i=0;i<n;i++){
		scan(tmp);
		v.push_back(tmp);
	}
};
inline void scan (vector<string> &v, int n){ //all words on the same line
	string tmp;
	for(int i=0;i<n;i++){
		scan(tmp);
		v.push_back(tmp);
		tmp.clear();
	}
};
inline void scanspace (vector<string> &v, int n){ //if several words on the same line
	string tmp;
	for(int i=0;i<n;i++){
		scanspace(tmp);
		v.push_back(tmp);
		tmp.clear();
	}
};
inline void scan(int a[],int b){
	for(int i=0;i<b;i++){
		scan(a[i]);
	}
};
inline void scan(long int a[],int b){
	for(int i=0;i<b;i++){
		scan(a[i]);
	}
};
inline void scan(long long int a[],int b){
	for(int i=0;i<b;i++){
		scan(a[i]);
	}
};
inline void scan(double a[],int b){
	for(int i=0;i<b;i++){
		scan(a[i]);
	}
};
inline void scan(char a[],int b){
	for(int i=0;i<b;i++){
		scan(a[i]);
	}
};
inline void scan(string a[],int b){
	for(int i=0;i<b;i++){
		scan(a[i]);
	}
};
inline void scanspace(string a[],int b){
	for(int i=0;i<b;i++){
		scanspace(a[i]);
	}
};
inline void scanasint(vector <int>& v){
	char c;
	while((c=getchar())=='\n'||c==' '||c=='\r');
	do{
		switch(c){
		case'\n':case'\r':case' ':return;
		default:v.push_back((int) c-'0');
		}
	}while((c=getchar())!=EOF);
};

inline void print(int a){ printf("%d",a); };
inline void print(long int a){ printf("%ld",a);}
inline void print(long long int a){printf("%lld",a);}
inline void print(double a,int nb=9){ printf("%.*lf",nb,a);};
inline void print(char c){cout<<c;};
inline void print(string s){cout<<s;};
inline void print(vector <int> v){
	vector<int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);
	}
};

inline void print(vector <bool> v){
	vector<bool>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		if(*it) {
			print('+');
		} else {
			print('-');
		}
	}
};
inline void print(vector <long int> v){
	vector<long int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);
	}
};
inline void print(vector <long long int> v){
	vector<long long int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);
	}
};
inline void print(vector <double> v){
	vector<double>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);
	}
};
inline void print(vector <char> v){
	vector<char>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);
	}
};
inline void print(vector <string> v){
	vector<string>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);
	}
};
inline void printspace(vector <int> v){
	vector<int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);space();
	}
};
inline void printspace(vector <long int> v){
	vector<long int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);space();
	}
};
inline void printspace(vector <long long int> v){
	vector<long long int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);space();
	}
};
inline void printspace(vector <double> v){
	vector<double>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);space();
	}
};
inline void printspace(vector <char> v){
	vector<char>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);space();
	}
};
inline void printspace(vector <string> v){
	vector<string>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);space();
	}
};
inline void println(vector <int> v){
	vector<int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);ln();
	}
};
inline void println(vector <long int> v){
	vector<long int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);ln();
	}
};
inline void println(vector <long long int> v){
	vector<long long int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);ln();
	}
};
inline void println(vector <double> v){
	vector<double>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);ln();
	}
};
inline void println(vector <char> v){
	vector<char>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);ln();
	}
};
inline void println(vector <string> v){
	vector<string>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);ln();
	}
};
inline void print(int a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);
	}
};
inline void print(long int a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);
	}
};
inline void print(long long int a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);
	}
};
inline void print(double a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);
	}
};
inline void print(char a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);
	}
};
inline void print(string a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);
	}
};
inline void printspace(int a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);space();
	}

}
inline void printspace(long int a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);space();
	}
};
inline void printspace(long long int a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);space();
	}
};
inline void printspace(double a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);space();
	}
};
inline void printspace(char a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);space();
	}
};
inline void printspace(string a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);space();
	}
};
inline void println(long int a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);ln();
	}
};
inline void println(long long int a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);ln();
	}
};
inline void println(double a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);ln();
	}
};
inline void println(char a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);ln();
	}
};
inline void println(string a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);ln();
	}
};








int test(){
	int N,K;
	long long int D;
	scan(D); scan(N);
	vector <int> v,k,s;
	vector <double> t;
	scan(v,2*N);
	double max,index;
	/*
	print(D);
ln();
*/
	for(int i=0;i<N;i++) {
		k.push_back(v[2*i]);
		s.push_back(v[2*i+1]);
		/*
		print(k[i]);
		ln();
		print(s[i]);
		ln();
*/
		t.push_back((D-k[i])/(double) s[i]);
		if(i==0) {
			max=(D-k[i])/(double) s[i];
			/*
			print("num");
			print(D-k[i]);
			print("den");
			print(s[i]);
			ln();
			print("max");
			print(max);
			ln();
*/
			index=i;
		} else {
			if((double) (D-k[i])/s[i]>max) {
				max=(D-k[i])/(double) s[i];
				index=i;
			}
		}
	}
	/*
	print("maxt");
	print(max);
	ln();
	*/
	double res;
	res=D/(double) max;
	print(res);
	//cout<<endl<<"N="<<N<<", K="<<K<<endl;

	return(0);
}

int init(){
	FILE* gg;
	gg= freopen("A-large.in","r",stdin);
	//A-small-attempt0.in
	if(gg==NULL) { cout<<"prob"; }
	freopen("output5.txt","w",stdout);

	return 0;
}

int main(){
	init();
	int t;
	scan(t);
	//print(t);

	for(int i=0;i<t;i++){
		printf("Case #%d: ",i+1);
		test();
		ln();
	}

}
