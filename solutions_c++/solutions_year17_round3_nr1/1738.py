#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <numeric>
#include <iomanip>


using namespace std;

typedef long long int lli;

const double PI  =3.141592653589793238463;


struct Pancake{

    lli R, H;



    bool operator<( const Pancake& other ) const
    {

        return this->R*this->H > other.R*other.H;

//                if(other.R == this->R){

//                    return this->R*this->H > other.R*other.H;


//                } else {

//                    return this->R > other.R;
//                }

   }
};

template <typename T>
vector<size_t> sort_indexes(const vector<T> &v) {

  // initialize original index locations
  vector<size_t> idx(v.size());
  iota(idx.begin(), idx.end(), 0);

  // sort indexes based on comparing values in v
  sort(idx.begin(), idx.end(),
       [&v](size_t i1, size_t i2) {return v[i1] < v[i2];});

  return idx;
}

lli solve(vector<Pancake>& cakes, lli K){


    auto sorted_cakes = sort_indexes(cakes);


    lli idx_best_radius_k = sorted_cakes[0];

    lli solution = 0;

    lli N = cakes.size();




    for(int i=0; i<K; i++){

        if(cakes[sorted_cakes[i]].R > cakes[idx_best_radius_k].R){

            idx_best_radius_k = sorted_cakes[i];
        }

        solution += 2*cakes[sorted_cakes[i]].R*cakes[sorted_cakes[i]].H;

    }

    solution += cakes[idx_best_radius_k].R*cakes[idx_best_radius_k].R;

    if( N > K){

        lli idx_best_radius_n = sorted_cakes[K];

        for(int i=K; i<N; i++){

            if(cakes[sorted_cakes[i]].R > cakes[idx_best_radius_n].R){

                idx_best_radius_n = sorted_cakes[i];
            }

        }


        if(cakes[idx_best_radius_n].R > cakes[idx_best_radius_k].R){

            lli contributed = 2*cakes[sorted_cakes[K-1]].R*cakes[sorted_cakes[K-1]].H;

            //if(idx_best_radius_k == sorted_cakes[K-1])
            contributed += cakes[idx_best_radius_k].R*cakes[idx_best_radius_k].R;

            lli potential = cakes[idx_best_radius_n].R*cakes[idx_best_radius_n].R +  2*cakes[idx_best_radius_n].R*cakes[idx_best_radius_n].H;


            if( potential > contributed){

                solution += potential;
                solution -= contributed;


            }

        }

    }


    return solution;
}

int main(int argc, char *argv[])
{
    int T;
    cin>>T;

    for(int c=1; c<=T; c++){

        lli N,K;
        cin>>N>>K;

        vector<Pancake> cakes;

        for(int i=0; i<N; i++){

            Pancake p;

            lli R,H;

            cin>>R>>H;

            p.R = R;
            p.H = H;

            cakes.push_back(p);


        }

        //std::cout << std::fixed;
        //std::cout << std::setprecision(6);
        //cout<<"Case #"<<c<<": "<< std::fixed<<std::setprecision(6)<<solve(K, S, D)<<endl;
        cout<<"Case #"<<c<<": "<< std::fixed<<std::setprecision(9)<< PI*solve(cakes, K) << endl;

    }
    return 0;
}
