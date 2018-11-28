#include<array>
#include<algorithm>
#include<iostream>
#include<set>
#include<string>
#include<vector>


int main(){
  int T; std::cin >> T;
  for(auto t=1; t<=T; ++t){
    int hd, ad, hk, ak, b, d; std::cin >> hd >> ad >> hk >> ak >> b >> d;
    auto r = 999999;
    for(auto nbd=0; nbd<=100; ++nbd)
      for(auto nbb=0; nbb<=100; ++nbb){
	auto nbt = -1;
	auto nbdr = nbd;
	auto nbbr = nbb;
	auto hdr = hd;
	auto hkr = hk;
	auto adc = ad;
	auto akc = ak;
	// auto ok = true;
	auto tt = 0;
	while(true){
	  ++tt;
	  	  if(tt > 1000){
	    tt = -1;
	    break;
	  }  

	  // std::cerr << tt << '\n';
	  // std::cerr << "myhealth " << hdr << '\n';
	  if(hkr<=adc){
	    // std::cerr << "KILL\n";
	    break;
	  }
	  
	  if(nbdr and (hdr > akc - d)){
	    akc -= d;
	    if(akc<0)
	      akc=0;
	    --nbdr;
	    hdr -= akc;
	    continue;
	  }
	  if(hdr<= akc){
	    hdr = hd;
	    hdr -= akc;
	    continue;
	  }

	  if(nbbr){
	    // std::cerr << "BUFF\n";
	    adc += b;
	    --nbbr;
	    hdr -= akc;
	    continue;
	  }


	  hkr -= adc;

	  hdr -= akc;

	  if(hdr <=0){
	    tt = -1;
	    break;
	  }
	  
	  if(tt > 1000){
	    tt = -1;
	    break;
	  }  
	}
	
	if(tt != -1)
	  nbt = tt;
	if(nbt != -1)
	  if(nbt < r)
	    r = nbt;
	// if(nbt==3){
	//   std::cerr << nbd <<  ' ' << nbb << '\n';
	// }
	  
      }
      
    if(r==999999)
      std::cout << "Case #" << t << ": IMPOSSIBLE" << '\n';
    else
      std::cout << "Case #" << t << ": " << r << '\n';
  }
}
