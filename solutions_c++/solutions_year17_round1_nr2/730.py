#include <set>
#include <vector>
#include <iostream>
#include <cstdio>

using namespace std;

int nIng;
multiset<int> ing[50];
int recipe[50];

int findSize(){
    int best = 10000000;
    for(int i=0;i<nIng;i++){
        int curr = *ing[i].begin();
        //Note we want, curr*10>=size*recipe[i]*9
        //curr*10/(recipe[i]*9)>=size
        int size = (curr*10)/(recipe[i]*9);
        if(size < best)
            best = size;
    }
    return best;
}


int greedy(){
    int count = 0;//number of successes
    int size = findSize();//size of the current kit
    while(true){
        //printf("TEST %d\n",size);
        bool good = true;
        vector<int> currPack;
        for(int i=0;i<nIng;i++){
            int curr = -1;
            do{
                if(ing[i].empty()){
                    return count;
                }
                curr = *ing[i].begin();
                ing[i].erase(ing[i].begin());
                //printf("CURR %d %d %d\n",curr*10,size*recipe[i]*9,size*recipe[i]*11);
            }while(curr*10<size*recipe[i]*9);//while too small get the next one
            if(curr*10>=size*recipe[i]*9 && curr*10<=size*recipe[i]*11){
                currPack.push_back(curr);
            }
            else{
                //reset the pack

                for(int j=0;j<currPack.size();j++){
                    //printf("RESET %d\n",currPack[j]);
                    ing[j].insert(currPack[j]);
                }
                ing[i].insert(curr);
                good = false;
                break;
            }
        }
        if(!good){
            size = max(findSize(),size+1);//worry about making progress
            //size++;//no ingredients of this size, find the next best size
        }
        else{
            count++;
        }
    }
}


int main(){
    int ncases;
    cin >> ncases;
    for(int c = 1;c<=ncases;c++){
        int nPacks;
        cin >> nIng >> nPacks;
        for(int i=0;i<nIng;i++){
            cin >> recipe[i];
        }
        for(int i=0;i<nIng;i++){
            ing[i] = multiset<int>();
            for(int j=0;j<nPacks;j++){
                int x;
                cin >> x;
                ing[i].insert(x);
            }
        }

        int res = greedy();
        printf("Case #%d: %d\n",c,res);
    }
}
