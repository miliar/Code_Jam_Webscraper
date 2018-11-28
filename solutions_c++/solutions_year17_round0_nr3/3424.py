#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#define LL  long long int 

void addEl(vector< LL > * v, vector< LL > * c, LL d , LL nd, LL * ma, LL * mi){
    LL d1, d2;

    if(0 == (d % 2)){
	d1 = d / 2;
	d2 = ((d - 1) / 2);

	if(v->end() == find(v->begin(), v->end(), d1)){
	    v->push_back(d1);
	    c->push_back(nd);
	}else{
	    (*c)[find(v->begin(), v->end(), d1) - v->begin()] += nd;
	}

	if(v->end() == find(v->begin(), v->end(), d2)){
	    v->push_back(d2);
	    c->push_back(nd);
	}else{
	    (*c)[find(v->begin(), v->end(), d2) - v->begin()] += nd;
	}

	*ma	= d1;
	*mi	= d2;
    }else{
	d1 = ((d - 1) / 2);

	if(v->end() == find(v->begin(), v->end(), d1)){
	    v->push_back(d1);
	    c->push_back(nd * 2);
	}else{
	    (*c)[find(v->begin(), v->end(), d1) - v->begin()] += (nd * 2);
	}

	*mi	= d1;
	*ma	= d1;
    }

}

int main(int argc, char ** argv){
    int nTest;

    ifstream inFile;
    ofstream outFile;

    inFile.open(argv[1]);
    outFile.open(argv[2]);

    inFile >> nTest;

    vector< LL > v;
    vector< LL > c;

    vector< LL > vt;
    vector< LL > ct;

    LL n;
    LL k;

    LL ma;
    LL mi;

    for(int idx = 0 ; nTest > idx ; idx++){
	inFile >> n;
	inFile >> k;

	v.clear();
	c.clear();

	v.push_back(n);
	c.push_back(1);

	while(0 < k){
	    vt.clear();
	    ct.clear();

	    for(int i = 0 ; v.size() > i ; i++){
		addEl(&vt, &ct, v[i], c[i], &ma, &mi);
		k   -= c[i];

		if(1 > k){
		    break;
		}
	    }
	    v = vt;
	    c = ct;

	}


	outFile << "Case #" << idx+1 <<": " << ma << " " <<  mi << endl;
    }

    inFile.close();
    outFile.close();

    return 0;
}

