#include <bits/stdc++.h>

#include "BRKGA/BRKGA.h"
#include "BRKGA/MTRand.h"
#include "BRKGA/Population.h"

#include "prettyprint.hpp"

using namespace std;

typedef long int		num;
typedef vector<num>		vn;
typedef list<num>		ln;
typedef bitset<16>		bs16;
//template <typename K,typename V> using ump = unordered_map<K,V>;
//using li=list<int>;

/* Streams */
string	BUF;
#define ssb					getline(cin,BUF);stringstream(BUF)
/* discard chain of chr *if* it's present */
//#define eat(ism,chr)	while(ism.peek()==chr){ism.get();}
#define eat(ism,chr)	while(ism.peek()==chr){ism.ignore();}
/* Misc */
#define fst		first
#define snd		second
#define NLM		numeric_limits<num>::max()
#define NLS		numeric_limits<streamsize>::max()
#define I3F		0x3f3f3f3f
#define EPS		1e-8
/* Containers */
#define Range(itr,Cnt)		const_iterator itr=Cnt.begin();itr!=Cnt.end();++itr
#define foreach(itr,Cnt)	for(typeof((Cnt).begin())itr=(Cnt).begin();itr!=(Cnt).end();++itr)
#define all(Cnt)			(Cnt).begin(), (Cnt).end()
#define in(elm,Cnt)			((Cnt).find(elm)!=(Cnt).end())
#define sz(Cnt)				((int)(Cnt.size()))
/* gcc-built-in */
#define gcd				__gcd
/* Debugging */
// -D DEBUG_BUILD
#define DEBUG_BUILD
#ifdef DEBUG_BUILD
#define DEBUG(x)	do{if(1){cerr<<x<<endl;}}while(0)
#define DBG(x)		do{cerr<<#x<<":\t["<<x<<"]"<<endl;}while(0)
#else
#define DBG(x)		;
#endif
/* Problem specific */
#define MAXN		1011
int V[MAXN];
int Vsize;

int c_1,c_2,c_3;
int c12,c23,c31;

int i2c(int i){
	int ret;
	if(i==0)ret=1;
	if(i==1)ret=2;
	if(i==2)ret=3;
	if(i==3)ret=12;
	if(i==4)ret=23;
	if(i==5)ret=31;
	return ret;
}

int get(int i){
	int ret;
	if(i==0)ret=c_1;
	if(i==1)ret=c_2;
	if(i==2)ret=c_3;
	if(i==3)ret=c12;
	if(i==4)ret=c23;
	if(i==5)ret=c31;
	return ret;
}
int* gr(int i){
	int* ret=&c_1;
	if(i==0)ret=&c_1;
	if(i==1)ret=&c_2;
	if(i==2)ret=&c_3;
	if(i==3)ret=&c12;
	if(i==4)ret=&c23;
	if(i==5)ret=&c31;
	return ret;
}
int getMax(){
	int reti,ret=-1;
	for(int i=0;i<6;++i){
		if(get(i) >= ret){
			ret = get(i);
			reti= (i);
		}
	}
	return reti;
}

char trans(int c){
	char ret='X';
	if(c== 1){ret='R';}
	if(c==12){ret='O';}
	if(c== 2){ret='Y';}
	if(c==23){ret='G';}
	if(c== 3){ret='B';}
	if(c==31){ret='V';}
	return ret;
}

bool incomp(int c1,int c2){
	int n1,n2;
	n1=(c1<9)?1:2;
	n2=(c2<9)?1:2;
	
	int p1[2];
	int p2[2];
	
	p1[0]=c1%10; c1/=10; if(c1){p1[1]=c1;}
	p2[0]=c2%10; c2/=10; if(c2){p2[1]=c2;}
	
	int i1,i2;
	for(i1=0;i1<n1;++i1)
	for(i2=0;i2<n2;++i2)
		if(p1[i1]==p2[i2])return true;
	return false;
}

int count_err(const std::vector<int>&P){
	int ret=0;
	for(int i=0;i<Vsize-1;++i){
		if(incomp(P[i],P[i+1]))ret++;
	}
	if(incomp(P[0],P[Vsize-1]))ret++;
	
	return ret;
}

vector< int > get_perm(const std::vector< double >& chromosome){
	std::vector< std::pair< double, int > > ranking(chromosome.size());
			
	for(unsigned i = 0; i < chromosome.size(); ++i) {
		ranking[i] = std::pair< double, int >(chromosome[i],V[i]);
	}
	// Here we sort 'permutation', which will then produce a permutation of [n] in pair::second:
	std::sort(ranking.begin(), ranking.end());

	// permutation[i].second is in {0, ..., n - 1}; a permutation can be obtained as follows
	vector< int > P;
	for(std::vector< std::pair< double, int > >::const_iterator i = ranking.begin();i != ranking.end(); ++i) {
		P.push_back(i->second);
	}

	return P;
}

/*GA*/
namespace Mh_BRKGA{
	
	class GADecoder{public:
		GADecoder(){} ~GADecoder(){}
		double decode(const std::vector< double >& chromosome)const{
			return count_err(get_perm(chromosome));
		}
		private:
	};
	
	void solve(int pN){
		const unsigned n = pN;		// size of chromosomes
		const unsigned p = n*10;	// size of population
		const double pe = 0.20;		// fraction of population to be the elite-set
		const double pm = 0.10;		// fraction of population to be replaced by mutants
		const double rhoe = 0.70;	// probability that offspring inherit an allele from elite parent
		const unsigned K = 3;		// number of independent populations
		const unsigned MAXT = 6;	// number of threads for parallel decoding
		
		GADecoder decoder;			// initialize the decoder
		
		const long unsigned rngSeed = 0;	// seed to the random number generator
		MTRand rng(rngSeed);				// initialize the random number generator
		
		// initialize the BRKGA-based heuristic
		BRKGA< GADecoder, MTRand > algorithm(n, p, pe, pm, rhoe, decoder, rng, K, MAXT);
		
		unsigned generation=0;		// current generation
		const unsigned X_INTVL=100;	// exchange best individuals at every 100 generations
		const unsigned X_NUMBER=2;	// exchange top 2 best
		const unsigned MAX_GENS=(n)*10;	// run for 1000 gens
		
		unsigned ADD_GENS = 0;			//mine
		unsigned pastGeneration=0;		//mine
		double pastFitness=pN*2;		//mine
		
		//for(auto CS:Metaheuristic::Candidates::hanke){algorithm.evolve((Instance::N)/2,sequence2chromosome(n,CS,Instance::Ts));}
		
		do{
			
			if(algorithm.getBestFitness()==0){break;}
			
			algorithm.evolve();	// evolve the population for one generation
			if((++generation) % X_INTVL == 0){
				algorithm.exchangeElite(X_NUMBER);	// exchange top individuals
			}
			
			/*mine*/
			if(algorithm.getBestFitness() != pastFitness){
				ADD_GENS += ((generation-pastGeneration)*2)/1;
				pastGeneration=generation;
				pastFitness   =algorithm.getBestFitness();
				std::cout<<"\rGEN:\t"<<generation<<"\t/"<<(MAX_GENS+ADD_GENS)<<"\tBF:\t"<<pastFitness<<std::endl;;
			}
			else{std::cout<<"\rGEN:\t"<<generation<<"\t/"<<(MAX_GENS+ADD_GENS)<<"\t"<<std::flush;}
		}while(generation<MAX_GENS+ADD_GENS/*&&pastFitness>Instance::LB*/);
		
		if(algorithm.getBestFitness()>=1){
			cout<<"IMPOSSIBLE";return;
		}
		
		vector< int > P = get_perm(algorithm.getBestChromosome()) ;
		//for(auto const&a:P){
		for(int a=0;a<Vsize;++a){
			cout<<trans(P[a]);
		}
		
		//DBG(algorithm.getBestChromosome());
		//DBG(algorithm.getBestFitness());
		//chromosome2sequence(Seq,algorithm.getBestChromosome(),(Instance::Ts));
	}
}



//namoral
int S[MAXN];
//vector<int> S;
// 0
// 1-did ok;
// 2-cant;
// 3-solved;
long long unsigned int out;
int solve(int p){//DBG(p);
	
	if((out++)>=Vsize*Vsize*8){return 2;}
	
	vector<pair<int,int> >vp(6);
			
	for(int i=0; i<6; ++i){vp[i]= std::pair<int,int>(-get(i),i);}
	std::sort(vp.begin(),vp.end());
	
	//DBG(vp);
	
	for(int i=0;i<6;++i){
		//DBG(i);
		
		if(vp[i].fst >= 0){continue;}
		
		//DBG( incomp(S[p-1] , i2c(vp[i].snd) ));
		
		if( incomp(S[p-1] , i2c(vp[i].snd) )){continue;}
		if(p==Vsize-1){
			if(incomp(S[0] , i2c(vp[i].snd) )){continue;}
		}
		
		//DBG(get(vp[i].snd));
		
		S[p] = i2c(vp[i].snd);
		*gr(vp[i].snd) -= 1;
		
		//DBG(get(vp[i].snd));
		
		if(p==Vsize-1){return 3;}
		
		int res=solve(p+1);
		
		if(res==3){//solved;
			return 3;
		}
		if(res==2){
			S[p] = 0;
			*gr(vp[i].snd) += 1;
		}
		
	}
	return 2;
}


int main(){ios::sync_with_stdio(false);
	int N_ct=0;
	cin>>N_ct;
	
	for(int ct=1;ct<=N_ct;++ct){
		int N;
		//   R   Y   B
		//int c_1,c_2,c_3;
		//int c12,c23,c31;
		//   O   G   V
		//        R      O      Y      G      B      V
		cin>>N>> c_1 >> c12 >> c_2 >> c23 >> c_3 >> c31;
		
		Vsize=N;
		
		//vector<int>V(N);
		/*
		int idx=0,i=0;
		for(i=0;i<c_1;++i){V[idx++]=1;}
		for(i=0;i<c_2;++i){V[idx++]=2;}
		for(i=0;i<c_3;++i){V[idx++]=3;}
		for(i=0;i<c12;++i){V[idx++]=12;}
		for(i=0;i<c23;++i){V[idx++]=23;}
		for(i=0;i<c31;++i){V[idx++]=31;}
		
		// N, R, O, Y, G, B, and V.
		
		cout<<"Case #"<<ct<<": ";
		Mh_BRKGA::solve(N);
		//seq
		cout<<endl;
		*/
		
		//small set
		/*int max_c;
		int max_c_n;
		
		if(c_1 >= c_2){
			max_c = 1;
			max_c_n = c_1;
		}
		else{
			max_c = 2;
			max_c_n = c_2;
		}
		if(max_c < c_3){
			max_c = 3;
			max_c_n = c_3;
		}
		cout<<"Case #"<<ct<<": ";
		if(max_c_n <= N/2){
			
		}
		else{
			cout<<"IMPOSSIBLE";
		}
		cout<<endl;*/
		
		//full
		out = 1;
		int seed=getMax();
		//S.resize(N,0);
		S[0] = i2c(seed);
		*gr(seed) -= 1;
		
		int res=solve(1);
		cout<<"Case #"<<ct<<": ";
		//DBG(res);
		if(res==3){
			for(int a=0;a<Vsize;++a){
				cout<<trans(S[a]);
			}
		}
		else{
			cout<<"IMPOSSIBLE";
		}
		cout<<endl;
	}
	return 0;
}
/* Terminal *//*
g++ -std=c++11 X.cpp -W -Wall -g -o exc
./exc > out.txt < in.X.txt
diff -ys --color out.txt 
time ./exc < in.X.txt		*/
