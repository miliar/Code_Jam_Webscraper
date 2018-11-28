#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long llu;

int solve(){
	int Ac, Aj;
	scanf("%d %d\n",&Ac,&Aj);
	int base = 0;
	vector<tuple<int,int,int>> Occ(Ac+Aj);
	vector<int> JJ;
	vector<int> JC;
	vector <int> CC;
	int Jall=720; int Call =720;
	for(int i=0;i<Ac;i++){
		cin >> get<0>(Occ[i])>>get<1>(Occ[i]);
		Jall -= get<1>(Occ[i]) - get<0>(Occ[i]);
		get<2>(Occ[i]) = 0; // james ha to watch
	}
	for(int i=Ac;i<Ac+Aj;i++){
		cin >> get<0>(Occ[i])>>get<1>(Occ[i]);
		Call -= get<1>(Occ[i]) - get<0>(Occ[i]);
		get<2>(Occ[i]) = 1; // cameron has to watch
	}
	sort(Occ.begin(),Occ.end());
	for(int i=1;i<Ac+Aj;i++){
		int size = get<0>(Occ[i]) - get<1>(Occ[i-1]);
		if(get<2>(Occ[i]) != get<2>(Occ[i-1])){
			base++;
			if(size != 0)JC.push_back(size);
		}else if(get<2>(Occ[i]) == 0 && size != 0){
			JJ.push_back(size);
		}else if(get<2>(Occ[i]) == 1 && size != 0){
			CC.push_back(size);
		}
	}
	int size = get<0>(Occ[0]) + 1440 - get<1>(Occ[Occ.size()-1]);
	//cout<<"\nS: "<<size<<endl;
	if(get<2>(Occ[0]) != get<2>(Occ[Occ.size()-1])){
		base++;
		if(size != 0)JC.push_back(size);
	}else if(get<2>(Occ[0]) == 0 && size != 0){
		JJ.push_back(size);
	}else if(get<2>(Occ[0]) == 1 && size != 0){
		CC.push_back(size);
	}
	sort(JJ.begin(),JJ.end());
	sort(CC.begin(),CC.end());
	sort(JC.begin(),JC.end());

	//cout<<endl<< "JJ: "<<JJ.size() <<" JC: "<<JC.size() << " CC: "<<CC.size()<<endl;
	//cout<<"Jall: "<<Jall<<" Call: "<<Call<<endl;

	while(Jall != 0 && JJ.size() != 0){
		if(Jall >= JJ[0]){
			Jall -= JJ[0];
			JJ.erase(JJ.begin());
		}else{
			JJ[0] -= Jall;
			Jall = 0;
		}
	}
	while(Jall != 0 && JC.size() != 0){
	//cout<<"JC :"<<JC[0] <<endl;

		if(Jall >= JC[0]){
			Jall -= JC[0];
			JC.erase(JC.begin());
		}else{
			JC[0] -= Jall;
			Jall = 0;
		}
	}
	while(Call != 0 && CC.size() != 0){
		if(Call >= CC[0]){
			Call -= CC[0];
			CC.erase(CC.begin());
		}else{
			CC[0] -= Call;
			Call = 0;
		}
	}
	while(Call != 0 && JC.size() != 0){
		if(Call >= JC[0]){
			Call -= JC[0];
			JC.erase(JC.begin());
		}else{
			JC[0] -= Call;
			Call = 0;
		}
	}
	if(Jall == 0 && Call == 0)return base;
	if(Jall != 0 && Call != 0){
		cout<< "Szar van a palacsintaban"<<endl;
		throw "Szar";
	}
	if(Jall != 0){
		return base + 2*CC.size();
	}else{
		return base + 2*JJ.size();
	}
}

int main() {
    int T;
    scanf("%d\n",&T);
    for(int i=1;i<=T;i++){
        printf("Case #%d: %d\n",i,solve());
    }
    return 0;
}
