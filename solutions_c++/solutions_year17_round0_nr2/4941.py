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
    vector <int> v,w;
    scanasint(v);
    int nb=v.size();
    int nb_init=nb;
    int sav,i=0;

    bool cont=true;
    bool g=true;
    sav=v[0];
    while(cont && nb>=1) {
    	if(nb==1) {
    		g=false;
    		cont=false;
    		w.push_back(v[i]);
    	}
    	if(g) {
    	i++;
    	if(v[i]>sav) {
    		w.push_back(v[i-1]);
    		sav=v[i];
        	nb=nb-1;
    	} else if(v[i]<sav){
    		cont=false;
    		w.push_back(v[i-1]-1);
    		for(int j=0;j<nb-1;j++) {
    			w.push_back(9);
    		}
    	} else {
    		bool cont2=true;
    		for(int j=0;j<nb_init-i and cont2;j++) {
    			if(v[i+j]>sav) {
    				for(int k=0;k<=j;k++){
    					w.push_back(v[i-1+k]);
    				}
    				nb=nb-j-1;
    				cont2=false;
    				sav=v[i+j];
    				i=i+j;
    			} else if(v[i+j]<sav) {
    				cont=false;
    				cont2=false;
    				w.push_back(v[i-1]-1);
    				for(int k=0;k<nb;k++){
    					w.push_back(9);
    				}
    			}
    		}

    		if(cont2) {
    			cont=false;
    			for(int k=0;k<nb;k++){
    			    w.push_back(v[i-1+k]);
    			}
    		}
    	}

    }
    }
    bool zero=true;
    for(int j=0;j<nb_init;j++) {
    	if(w[j]!=0 or !zero){
    		print(w[j]);
    		zero=false;
    	}
    }
    return(0);
}

int init(){
	FILE* gg;
    gg= freopen("B-large.in","r",stdin);
    if(gg==NULL) { cout<<"prob"; }
    freopen("outputlarge.txt","w",stdout);
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
