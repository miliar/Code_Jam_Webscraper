
#include <iostream>
#include <vector>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int tsc=0; tsc<T; tsc++){
		cout << "Case #"<<tsc+1<<": ";

		int N,R,O,Y,G,B,V;
		cin >> N >> R >> O >> Y >> G >> B >> V;

		if(V == Y && V+Y==N){
			for(int i=0; i<N/2; i++){
				cout << "YV";
			}
			cout << endl;
			continue;
		}
		if(G == R && R+G==N){
			for(int i=0; i<N/2; i++){
				cout << "RG";
			}
			cout << endl;
			continue;
		}
		if(O == B && O+B==N){
			for(int i=0; i<N/2; i++){
				cout << "OB";
			}
			cout << endl;
			continue;
		}

		if((V != 0 && V+1 > Y) || (G != 0 && G+1 > R) || (O != 0 && O+1 > B)){
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		
		vector<vector<char> > Ys;

		vector<char> tmp;
		if(Y > 0){
		tmp.push_back('Y');
		Y--;
		while(V > 0){
			tmp.push_back('V');
			tmp.push_back('Y');
			V--;
			Y--;
		}
		Ys.push_back(tmp);
		tmp.clear();
		tmp.push_back('Y');
		while(Y > 0){
			Ys.push_back(tmp);
			Y--;
		}
		}

		vector<vector<char> > Rs;

		tmp.clear();
		if(R > 0){
		tmp.push_back('R');
		R--;
		while(G > 0){
			tmp.push_back('G');
			tmp.push_back('R');
			G--;
			R--;
		}
		Rs.push_back(tmp);
		tmp.clear();
		tmp.push_back('R');
		while(R > 0){
			Rs.push_back(tmp);
			R--;
		}
		}

		vector<vector<char> > Bs;

		tmp.clear();
		if(B > 0){
		tmp.push_back('B');
		B--;
		while(O > 0){
			tmp.push_back('O');
			tmp.push_back('B');
			O--;
			B--;
		}
		Bs.push_back(tmp);
		tmp.clear();
		tmp.push_back('B');
		while(B > 0){
			Bs.push_back(tmp);
			B--;
		}
		}
//
//		cout << "Rs: ";
//		for(auto it=Rs.begin(); it!=Rs.end(); it++){
//		for(auto jt=it->begin(); jt!=it->end(); jt++){
//			cout << *jt;
//		}
//		cout << " ";
//		}
//		cout << endl;
//
//		cout << "Ys: ";
//		for(auto it=Ys.begin(); it!=Ys.end(); it++){
//		for(auto jt=it->begin(); jt!=it->end(); jt++){
//			cout << *jt;
//		}
//		cout << " ";
//		}
//		cout << endl;
//
//		cout << "Bs: ";
//		for(auto it=Bs.begin(); it!=Bs.end(); it++){
//		for(auto jt=it->begin(); jt!=it->end(); jt++){
//			cout << *jt;
//		}
//		cout << " ";
//		}
//		cout << endl;

		int n = Ys.size() + Bs.size() + Rs.size();
		if(Ys.size() > n/2 || Bs.size() > n/2 || Rs.size() > n/2) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		vector<vector<char> > tmp_ans;

		while(!Ys.empty() && !Bs.empty()){
			tmp_ans.push_back(Ys.back());
			tmp_ans.push_back(Bs.back());
			Ys.pop_back();
			Bs.pop_back();
		}

//		cout << "tmp_ans: ";
//		for(auto it=tmp_ans.begin(); it!=tmp_ans.end(); it++){
//		for(auto jt=it->begin(); jt!=it->end(); jt++){
//			cout << *jt;
//		}
//		cout << " ";
//		}
//		cout << endl;

		vector<vector<char> > f = Bs;
		vector<vector<char> > b = Rs;
		if(Ys.empty()){
			b = Bs;
			f = Rs;
		}else{
			b = Rs;
			f = Ys;
		}

		while(!f.empty() && !b.empty()){
			tmp_ans.push_back(f.back());
			tmp_ans.push_back(b.back());
			f.pop_back();
			b.pop_back();
		}

		if(b.empty()) b = f;

//		cout << "b: ";
//		for(auto it=b.begin(); it!=b.end(); it++){
//		for(auto jt=it->begin(); jt!=it->end(); jt++){
//			cout << *jt;
//		}
//		cout << " ";
//		}
//		cout << endl;

		int i=0;
		while(i < tmp_ans.size() && !b.empty()){
			for(auto it=tmp_ans[i].begin(); it!=tmp_ans[i].end(); it++){
				cout << *it;
			}
			for(auto it=b.back().begin(); it!=b.back().end(); it++){
				cout << *it;
			}
			b.pop_back();
			i++;
		}

		while(i < tmp_ans.size()){
			for(auto it=tmp_ans[i].begin(); it!=tmp_ans[i].end(); it++){
				cout << *it;
			}
			i++;
		}
		cout << endl;
	}
}

		/*
		vector<pair<int,char> > c;
		c.push_back(pair<int,char>(R,'R'));
		c.push_back(pair<int,char>(O,'O'));
		c.push_back(pair<int,char>(Y,'Y'));
		c.push_back(pair<int,char>(G,'G'));
		c.push_back(pair<int,char>(B,'B'));
		c.push_back(pair<int,char>(V,'V'));

		vector<char> res;
		pair<int,char> f,b;
		f = pair<int,char>(0,'a');
		b = pair<int,char>(0,'a');
		while(!c.empty()){
			while(!c.empty() && f.first==0) f = c.back(), c.pop_back();
			while(!c.empty() && b.first==0) b = c.back(), c.pop_back();

			while(f.first > 0 && b.first > 0){
				f.first--;
				b.first--;
				res.push_back(f.second);
				res.push_back(b.second);
			}
		}

		vector<char> ans;
		int i=0; 
		while(f.first > 0){
			ans.push_back(res[i++]);
			ans.push_back(f.second);
			f.first--;
		}
		while(i < res.size()){
			ans.push_back(res[i++]);
		}

		cout << "Case #"<<tsc+1<<": ";
		for(auto it=ans.begin(); it!=ans.end(); it++){
			cout << *it;
		}
		cout << endl;
		*/
