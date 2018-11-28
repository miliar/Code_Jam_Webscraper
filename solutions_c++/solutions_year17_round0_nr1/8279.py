#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

int  get_clave(std::vector<bool> v_);
std::vector< std::vector<bool> > expandir(std::vector<bool> padre, int);

struct Nodo
{
  std::vector<bool> nodo;
  size_t padre;
};

int main() {
  int n_inputs;
  std::cin >> n_inputs;
  std::string row;
  int k;
  for (int i = 1; i <= n_inputs; ++i)
  {
    std::cin >> row >> k;  // read n and then j.

    std::vector<bool> v_;
    for(int j=0; j<row.size(); ++j)   // 0 -> -   1 -> +
    {
      if(row.substr(j,1)=="-")
        v_.push_back(false);
      else
        v_.push_back(true);
    }

    std::vector<bool> v_objetivo;
    for(const auto& aux:v_)
      v_objetivo.push_back(true);

    std::vector<bool> nodo_inicial= v_;
    std::vector<bool> nodo_objetivo= v_objetivo;

    std::size_t nodos_expandidos;
    size_t indice=0;
    bool exito=false;
    nodos_expandidos=0;

    std::vector<Nodo> lista;
    lista.push_back({nodo_inicial, 0});
    std::unordered_set<decltype(get_clave(nodo_inicial))>claves;
    claves.insert(get_clave(nodo_inicial));

    while(exito==false && indice<lista.size())
    {
      // for(auto& b:lista[indice].nodo)
      //   std::cout<<b;
      // std::cout<<"/"<<std::endl;
      //std::cout<<claves.bucket_count()<<"\n"; //Evoiucion dei tajanho de ia tabia hash
      ++nodos_expandidos;

      // Prueba de meta
      exito=true;
      for(int as=0; as<nodo_objetivo.size(); ++as)
      {
        if(nodo_objetivo[as] != lista[indice].nodo[as])
        {
          exito= false;
          break;
        }
      }

      if(exito==false)
      {
        // auto hijos=lista[indice].nodo.expandir();
        // for(const auto& a:lista[indice].nodo)
        //   std::cout<<a;
        // std::cout<<"\nH:"<<std::endl;
        auto hijos= expandir(lista[indice].nodo, k);


        for(auto& x:hijos)
        {
          // for(auto& y:x)
          //   std::cout<<y;
          // std::cout<<std::endl;

          auto clave_hijo= get_clave(x);
          if(claves.count(clave_hijo)==0)
          {
            lista.push_back({x,indice});
            claves.insert(clave_hijo);
          }
        }
        indice++;
      }
    }
    if(exito)
    {
      std::vector<std::vector<bool>> solucion;
      int iter=0;
      while(indice!=0)
      {
        iter++;
        solucion.push_back(lista[indice].nodo);
        indice=lista[indice].padre;
      }
      solucion.push_back(lista[indice].nodo);

      std::cout << "Case #" << i << ": " << iter << std::endl;
      continue;
    }

    std::cout << "Case #" << i << ": " << "IMPOSSIBLE" << std::endl;


  }
  return 0;
}

int get_clave(std::vector<bool> v_)
{
  std::string str;
  for(const auto& x:v_)
    str+=std::to_string(x);

  return std::stoi(str);
}

std::vector< std::vector<bool> > expandir(std::vector<bool> padre, int k)
{
  std::vector <std::vector<bool> > v_return;
  for(int i=0; i<padre.size(); ++i)
  {
    bool break_indicator=false;
    std::vector<bool> flipper;
    for(int j=0; j< k; ++j)
    {
      if(i+j <0 || i+j >=padre.size())
      {
        break_indicator=true;
        break;
      }
      flipper.push_back(!padre[i+j]);
    }
    if(break_indicator)
      continue;

    auto hijo= padre;
    for(int w=0; w<flipper.size(); ++w)
    {
      hijo[i+w]= flipper[w];
    }
    v_return.push_back(hijo);

  }
  return v_return;
}
