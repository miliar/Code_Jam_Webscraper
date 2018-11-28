#include <iostream>
#include <fstream>

using namespace std;

struct adat{
    int helyd, ember,min,max;
};

int Lh(int *sor,int k){
    int ossz=0;
    for(int l=0;l<k;l++){
        if(sor[l]==0)
            ossz++;
        else
            ossz=0;
    }
    return ossz;
}

int Rh(int *sor,int k,int veg){
    int ossz=0;
    for(int l=veg-1;l>k;l--){
        if(sor[l]==0)
            ossz++;
        else
            ossz=0;
    }
    return ossz;
}

int mins(int *l, int veg){
    int lk=l[1];
    for(int m=2;m<veg;m++){
        if(l[m]<lk)
            lk=l[m];
    }
    return lk;
}

int maxs(int *l, int veg){
    int lk=l[1];
    for(int m=2;m<veg;m++){
        if(l[m]>lk)
            lk=l[m];
    }
    return lk;
}

int minp(int egy, int ketto){
    if(egy<=ketto)
        return egy;
    else
        return ketto;
}

int maxp(int egy, int ketto){
    if(egy>=ketto)
        return egy;
    else
        return ketto;
}

int main()
{
    ifstream f;
    int darab;
    f.open("be.txt");
    f >> darab;
    adat *adatok=new adat[darab];
    for(int i=0;i<darab;i++){
        f >> adatok[i].helyd;
        f >> adatok[i].ember;
    }
    f.close();
    for(int i=0;i<darab;i++){
        if(adatok[i].helyd==adatok[i].ember){
            adatok[i].min=0;
            adatok[i].max=0;
        }else if(adatok[i].ember==1){
            if(adatok[i].helyd%2==0){
                adatok[i].min=adatok[i].helyd/2-1;
                adatok[i].max=adatok[i].helyd/2;
            }else{
                adatok[i].min=adatok[i].helyd/2;
                adatok[i].max=adatok[i].helyd/2;
            }
        }else{
            int *sor=new int[adatok[i].helyd+2];
            for(int j=0;j<adatok[i].helyd+1;j++)
                sor[j]=0;
            sor[0]=1;
            sor[adatok[i].helyd+1]=1;
            int *ls=new int[adatok[i].helyd+2];
            int *rs=new int[adatok[i].helyd+2];
            int *legk=new int[adatok[i].helyd+2];
            for(int j=0;j<adatok[i].ember;j++){
                for(int k=0;k<adatok[i].helyd+2;k++){
                    if(sor[k]==0){
                        ls[k]=Lh(sor,k);
                        rs[k]=Rh(sor,k,adatok[i].helyd+2);
                        legk[k]=minp(ls[k],rs[k]);
                    }else{
                        ls[k]=-1;
                        rs[k]=-1;
                        legk[k]=-1;
                    }
                }
                int ln=maxs(legk,adatok[i].helyd+2);
                int lndb=0, lnh;
                for(int k=1;k<adatok[i].helyd+2;k++){
                    if(legk[k]==ln){
                        lndb++;
                        lnh=k;
                    }
                }
                if(lndb==1){
                    adatok[i].max=maxp(ls[lnh],rs[lnh]);
                    adatok[i].min=minp(ls[lnh],rs[lnh]);
                    sor[lnh]=1;
                }else{
                    int *lkh=new int[adatok[i].helyd+2];
                    for(int k=0;k<adatok[i].helyd+2;k++){
                        if(legk[k]==ln)
                            lkh[k]=1;
                        else
                            lkh[k]=0;
                    }
                    for(int k=1;k<adatok[i].helyd+2;k++){
                        if((sor[k]==0) && (lkh[k]==1)){
                            legk[k]=maxp(ls[k],rs[k]);
                        }else{
                            legk[k]=-1;
                        }
                    }
                    int ln=maxs(legk,adatok[i].helyd+2);
                    int lnh=0;
                    while(legk[lnh]!=ln)
                        lnh++;
                    adatok[i].max=maxp(ls[lnh],rs[lnh]);
                    adatok[i].min=minp(ls[lnh],rs[lnh]);
                    sor[lnh]=1;
                }
            }
            cout <<"."<<endl;
        }
    }
    ofstream g;
    g.open("ki.txt");
    for(int i=0;i<darab;i++)
        g <<"Case #"<<i+1<<": "<<adatok[i].max<<" "<<adatok[i].min<<endl;
    g.close();
    return 0;
}

























