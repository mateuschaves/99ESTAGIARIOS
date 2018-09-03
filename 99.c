#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

typedef struct {
    char name[60], rg[20], phone[20], address[200], add[300], area[200], schedule_begin[20], schedule_end[20];
    int id;
} intern;

intern trainees[1024];

void create(int q);
int menu();

void main(void){
    setlocale(LC_ALL, "");
    int q, m = 0;
    do{
        m = menu();
        switch(m){
            case 1:
                create(q);
                q++;
                break;
        }
    }while(m != 6);
    system("pause");
}

int menu(){
    setlocale(LC_ALL, "");
    int menu;
    printf("\n1 - Cadastrar novo estagiário\n");
    printf("2 - Editar um estagiário\n");
    printf("3 - Mostrar um estagiário\n");
    printf("4 - Deletar um estagiário\n");
    printf("5 - Mostrar todos os estagiários\n");
    printf("6 - Sair\n");
    scanf("%d", &menu);
    return menu;
}

void create(int q){
    printf("\n\nCADASTRANDO O ESTAGIÁRIO NÚMERO %d\n\n", q+1);
    printf("Nome: ");
    fflush(stdin);
    gets(trainees[q].name);
    printf("RG: ");
    fflush(stdin);
    gets(trainees[q].rg);
    printf("Telefone: ");
    fflush(stdin);
    gets(trainees[q].phone);
    printf("Endereço: ");
    fflush(stdin);
    gets(trainees[q].address);
    printf("Area de formacao: ");
    fflush(stdin);
    gets(trainees[q].area);
    printf("Horario de início: ");
    fflush(stdin);
    gets(trainees[q].schedule_begin);
    printf("Horario de término: ");
    fflush(stdin);
    gets(trainees[q].schedule_end);
    printf("Matrícula: ");
    fflush(stdin);
    scanf("%d", &trainees[q].id);
}